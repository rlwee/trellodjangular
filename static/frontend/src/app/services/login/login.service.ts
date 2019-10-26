import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class LoginService {
  loginUrl:string = 'http://127.0.0.1:8000/api/users/';

  constructor(private http: HttpClient) { }

  // loginUser(userData){
  //   return this.http.get(this.loginUrl, userData);
  // }

  loginUser(username:string, password:string){
    let val = {username:username, password:password}
    console.log(username)
    return this.http.post(this.loginUrl, val);
  }


}
