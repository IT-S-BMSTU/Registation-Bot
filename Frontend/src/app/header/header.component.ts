import {Component, Input} from '@angular/core';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.scss']
})
export class HeaderComponent {
  @Input() routerOutletName:  string = '';
  headerTitles: { [key: string]: string } = {
    'list': 'Личный кабинет',
    'creation': 'Создать нового бота'
  };
}
