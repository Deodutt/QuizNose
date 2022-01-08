describe('Title', () => {
    it('has the right title', () => {
        cy.visit('http://localhost:8080')

        cy.get('h1')
            .invoke('text')
            .should("equal", "Welcome to Quiz")
        Cypress.Screenshot.defaults({
        capture: 'runner',
        })
        cy.screenshot();
    });
});