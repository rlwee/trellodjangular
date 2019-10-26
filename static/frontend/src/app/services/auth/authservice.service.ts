import { Injectable } from '@angular/core';
import * as _ from 'lodash';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class AuthserviceService {

  constructor(private http: HttpClient) { }


  getToken(){
    let d = (<any>window).localStorage;
    if(!d) return null;
  
    return JSON.parse(d)
  }

}


