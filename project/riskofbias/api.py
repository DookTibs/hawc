from __future__ import absolute_import

from rest_framework import filters
from rest_framework import viewsets
from rest_framework_extensions.mixins import ListUpdateModelMixin

from assessment.api import AssessmentLevelPermissions, AssessmentEditViewset,\
    AssessmentViewset, DisabledPagination, InAssessmentFilter, RequiresAssessmentID
from utils.api import BulkIdFilter
from utils.views import TeamMemberOrHigherMixin

from . import models, serializers


class RiskOfBiasDomain(viewsets.ReadOnlyModelViewSet):
    assessment_filter_args = 'assessment'
    model = models.RiskOfBiasDomain
    pagination_class = DisabledPagination
    permission_classes = (AssessmentLevelPermissions,)
    filter_backends = (InAssessmentFilter, filters.DjangoFilterBackend)
    serializer_class = serializers.AssessmentDomainSerializer

    def get_queryset(self):
        return self.model.objects.all().prefetch_related('metrics')


class RiskOfBias(viewsets.ModelViewSet):
    assessment_filter_args = 'study__assessment'
    model = models.RiskOfBias
    pagination_class = DisabledPagination
    permission_classes = (AssessmentLevelPermissions,)
    filter_backends = (InAssessmentFilter, filters.DjangoFilterBackend)
    serializer_class = serializers.RiskOfBiasSerializer

    def get_queryset(self):
        return self.model.objects.all()\
            .prefetch_related('study', 'author', 'scores__metric__domain')


class RiskOfBiasScore(viewsets.ReadOnlyModelViewSet):
    model = models.RiskOfBiasScore
    pagination_class = DisabledPagination
    serializer_class = serializers.RiskOfBiasScoreChoiceSerializer

    def get_queryset(self):
        return self.model.objects.all()[:1]


class AssessmentMetricViewset(AssessmentViewset):
    model = models.RiskOfBiasMetric
    serializer_class = serializers.AssessmentMetricChoiceSerializer
    pagination_class = DisabledPagination
    assessment_filter_args = "domain__assessment"

    def get_queryset(self):
        return self.model.objects.all()


class AssessmentMetricScoreViewset(AssessmentViewset):
    model = models.RiskOfBiasMetric
    serializer_class = serializers.AssessmentMetricScoreSerializer
    pagination_class = DisabledPagination
    assessment_filter_args = "domain__assessment"

    def get_queryset(self):
        return self.model.objects.all()


class AssessmentScoreViewset(AssessmentEditViewset, TeamMemberOrHigherMixin, ListUpdateModelMixin):
    model = models.RiskOfBiasScore
    serializer_class = serializers.AssessmentRiskOfBiasScoreSerializer
    pagination_class = DisabledPagination
    assessment_filter_args = 'metric__domain_assessment'
    filter_backends = (BulkIdFilter, )

    def get_assessment(self, request, *args, **kwargs):
        assessment_id = request.GET.get('assessment_id', None)
        if assessment_id is None:
            raise RequiresAssessmentID

        return get_object_or_404(self.parent_model, pk=assessment_id)

    def get_queryset(self):
        return self.model.objects.all()
