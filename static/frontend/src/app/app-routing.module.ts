import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Routes, RouterModule } from '@angular/router';

import { LoginComponent } from './components/login/login.component';

const routes: Routes = [
                      {path: 'users', component: LoginComponent}
                       ];

@NgModule({
  declarations: [],
  imports: [CommonModule,
            RouterModule.forRoot(routes)],

  exports: [
            RouterModule
           ]
})
export class AppRoutingModule { }
