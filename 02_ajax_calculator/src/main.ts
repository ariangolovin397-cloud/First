import './style.css'
import { setupCounter } from './counter.ts'


const counter = document.querySelector<HTMLButtonElement>('#counter')!;
setupCounter(counter);
