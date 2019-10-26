import { Component, OnInit, Input } from '@angular/core';
import { FormGroup, FormControl, Validators } from '@angular/forms';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';
import { LoginService } from '../../services/login/login.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

    form: FormGroup = new FormGroup({
    username: new FormControl('', Validators.required),
    password: new FormControl('', Validators.required),
  });


  constructor(private httpClient: HttpClient, private router:Router, private auth: LoginService ) { }

  ngOnInit() {
  }

  validate(){
    console.log(this.form);
  }

  loginUser():void{
    this.auth.loginUser(this.form.value.username, this.form.value.password).subscribe((success) => {
      console.log('test');

      if(success["token"] != null){
        console.log(success['token'])
        localStorage.setItem('Auth', success["token"])
        this.router.navigate(['/']);
        console.log('Logged in');
      }

    });

  }

}
