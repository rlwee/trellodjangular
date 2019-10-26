import * as _ from 'lodash';
import { Injectable } from '@angular/core';
import {HttpEvent,
        HttpInterceptor,
        HttpHandler,
        HttpRequest,
        HttpHeaders} from '@angular/common/http';
import { Observable } from 'rxjs';
import { AuthserviceService } from './services/auth/authservice.service';
import { tap } from 'rxjs/operators';
import 'rxjs/add/observable/throw';
import 'rxjs/add/operator/catch';


@Injectable({
    providedIn: 'root'
})
export class Interceptor implements HttpInterceptor{
    
    constructor(private auth:AuthserviceService){}

    intercept (r: HttpRequest<any>, n: HttpHandler) : Observable <HttpEvent <any>> {
        let req = r.clone({
            headers: r.headers.set('Authorization', this.Token())
        });

        return n.handle(req).pipe(tap(
            resp => {
                if (resp instanceof Interceptor) return resp;
            }
        ));
    }

    Token(){
        const t = _.get(this.auth.getToken(), ['token'], null);
        return `Token ${t}`;
    }
}
