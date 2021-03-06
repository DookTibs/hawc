import * as types from 'robScoreCleanup/constants';

const defaultState = {
    isFetching: false,
    isLoaded: false,
    selected: null,
    items: [],
};

function metrics(state=defaultState, action) {

    switch(action.type){

    case types.REQUEST_METRIC_OPTIONS:
        return Object.assign({}, state, {
            isFetching: true,
        });

    case types.RECEIVE_METRIC_OPTIONS:
        return Object.assign({}, state, {
            isFetching: false,
            isLoaded: true,
            items: action.metrics,
        });

    case types.SELECT_METRIC:
        return Object.assign({}, state, {
            selected: action.metric,
        });

    default:
        return state;
    }
}

export default metrics;
