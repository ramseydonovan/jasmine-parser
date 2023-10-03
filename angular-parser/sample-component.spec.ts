

describe( () => {
  let component: BannerComponent;
let fixture: ComponentFixture<BannerComponent>;
let h1: HTMLElement;

    beforeEach(() => {
        TestBed.configureTestingModule({
            declarations: [ BannerComponent ],
            providers: [
            { provide: ComponentFixtureAutoDetect, useValue: true },
            { provide: SixthService, useValue: true }
            ]
        });

    fixture = TestBed.createComponent(BannerComponent);
    component = fixture.componentInstance; // BannerComponent test instance
    h1 = fixture.nativeElement.querySelector('h1');
    });

  it('should display original title', () => {
    // Hooray! No `fixture.detectChanges()` needed
    expect(h1.textContent).toContain(comp.title);
  });
  
  it('should still see original title after comp.title change', () => {
    const oldTitle = comp.title;
    comp.title = 'Test Title';
    // Displayed title is old because Angular didn't hear the change :(
    expect(h1.textContent).toContain(oldTitle);
  });
  
  it('should display updated title after detectChanges', () => {
    comp.title = 'Test Title';
    fixture.detectChanges(); // detect changes explicitly
    expect(h1.textContent).toContain(comp.title);
  });

});


describe( (' second describe') => {
    let component: BannerComponent;
  let fixture: ComponentFixture<BannerComponent>;
  let h1: HTMLElement;
  
      beforeEach(() => {
          TestBed.configureTestingModule({
              declarations: [ BannerComponent ],
              providers: [
              { provide: ComponentFixtureAutoDetect, useValue: true }
              ]
          });
    
    it('should display updated title after detectChanges', () => {
      comp.title = 'Test Title';
      fixture.detectChanges(); // detect changes explicitly
      expect(h1.textContent).toContain(comp.title);
    });
  
  });

