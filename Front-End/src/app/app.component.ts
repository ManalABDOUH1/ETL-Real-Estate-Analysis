import { Component } from '@angular/core';

@Component({
    selector: 'app-root',
    templateUrl: './app.component.html',
    styleUrls: ['./app.component.css']
})
export class AppComponent {
    title = 'D3.js with Angular!';
    sideBarOpen = true;

    sideBarToggler() {
      this.sideBarOpen = !this.sideBarOpen;
    }

    examples = [
        {
            title: 'Pricec per Outside',
            route: '/line-chart'
        },
        {
            title: 'Price per City',
            route: '/bar-chart'
        },
        {
            title: 'Price per Outside (Location)',
            route: '/stacked-bar-chart'
        },
        {
            title: 'City %',
            route: '/pie-chart'
        },
        {
            title: 'City ',
            route: '/donut-chart'
        }
    ];

}
