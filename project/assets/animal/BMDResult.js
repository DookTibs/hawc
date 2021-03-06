import EndpointCriticalDose from './EndpointCriticalDose';


class BMDResult extends EndpointCriticalDose {
    constructor(endpoint, span, type, show_units, show_url){
        super(...arguments);
        this.show_url = show_url;
    }

    display(){
        var txt,
            bmd = this.endpoint.data.bmd,
            currentUnits = this.endpoint.dose_units_id,
            bmdUnits = this.endpoint.data.bmd.dose_units;

        if (currentUnits == bmdUnits){
            txt = bmd.output[this.type].toHawcString();
            if (this.show_units){
                txt = txt + ' {0}'.printf(this.endpoint.dose_units);
            }
            if (this.show_url){
                txt = txt + ' <a href="{0}">(view details)</a>'.printf(bmd.url);
            }
        } else {
            txt = '-';
        }
        return this.span.html(txt);
    }
}


export default BMDResult;
