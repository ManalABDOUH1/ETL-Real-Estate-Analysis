import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { MatMenuModule, MatSidenavModule } from '@angular/material';

import { AppComponent } from './app.component';
import { LineChartComponent } from './01_line_chart/line-chart.component';
import { MultiSeriesComponent } from './02_multi_series_line_chart/multi-series.component';
import { BarChartComponent } from './03_bar_chart/bar-chart.component';
import { StackedBarChartComponent } from './04_stacked_bar_chart/stacked-bar-chart.component';
import { BrushZoomComponent } from './05_brush_zoom/brush-zoom.component';
import { PieChartComponent } from './06_pie_chart/pie-chart.component';
import { DonutChartComponent } from './07_donut_chart/donut-chart.component';
import { HeaderComponent } from './header/header.component';
import { HomeComponent } from './home/home.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { SidenavComponent } from './sidenav/sidenav.component';
//
import { AppRoutingModule } from './app-routing.module';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatIconModule } from '@angular/material/icon';
import { MatDividerModule } from '@angular/material/divider';
import { MatListModule } from '@angular/material/list';
import { LocationComponent } from './location/location.component';

const appRoutes: Routes = [
    { path: 'line-chart', component: LineChartComponent },
    { path: 'multi-series', component: MultiSeriesComponent },
    { path: 'bar-chart', component: BarChartComponent },
    { path: 'stacked-bar-chart', component: StackedBarChartComponent },
    { path: 'brush-zoom', component: BrushZoomComponent },
    { path: 'pie-chart', component: PieChartComponent },
    { path: 'donut-chart', component: DonutChartComponent },
    { path: 'dashboard', component: DashboardComponent },
    { path: 'app-home', component: HomeComponent },
    { path: 'app-location', component: LocationComponent },

    { path: '',
        redirectTo: '/dashboard',
        pathMatch: 'full'
    },
    { path: '**', component: DashboardComponent }
];

@NgModule({
    declarations: [
        AppComponent,
        LineChartComponent,
        MultiSeriesComponent,
        BarChartComponent,
        StackedBarChartComponent,
        BrushZoomComponent,
        PieChartComponent,
        DonutChartComponent,
        HeaderComponent,
        HomeComponent,
        DashboardComponent,
        SidenavComponent,
        LocationComponent,
    ],
    imports: [
        BrowserModule,
        BrowserAnimationsModule,
        RouterModule.forRoot(appRoutes),
        MatMenuModule,
        MatSidenavModule,
        BrowserModule,
        AppRoutingModule,
        BrowserAnimationsModule,
        // * MATERIAL IMPORTS
        MatSidenavModule,
        MatToolbarModule,
        MatMenuModule,
        MatIconModule,
        MatDividerModule,
        MatListModule,
    ],
    providers: [],
    bootstrap: [AppComponent]
})
export class AppModule { }
