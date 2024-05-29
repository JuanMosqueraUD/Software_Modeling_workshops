# Workshop 4

This is a workshop related to the last update of the vehicle catalog

## Requirements


 1. Application is not registering in a good way the actions of users. Check why is this
 failing and fix it.
 2. There are just test cases for engines sub-system. You should add tests for all the other
 modules.
 3. Check for code smells across the code, use pylint is a good idea. However, it is not
 enough, you must fix all the issues found after make a code review.
 4. Code should be good formated and with the best comments you could write/update
 from the code.
 5. Check the logs in order to figure out the functionalities with bad performance, and
 fix them.
 
 6. Add a new feature to the application, now it should be able for users to be subscribed
 to a newsletter using an email. The newsletter should be sent by the admin anytime
 he/she wants, just with the information with the last five vehicles created (if there
 are less than five, just sent the complete catalog).
 7. Cache memory is still do not implemented. It means, the last three searches made in
 the system shloud be saved into memory just to avoid make the same search again.
 Every time a vehicle is added, this memory should be shuffed.
 8. Maybe an admin could make an error. So, provide an option to recovery the last
 vehicle deleted.
 9. Add a new type of engine: a hybrid engine. This engine should have a new attribute:
 electric_power (in Watts). The values for attributes of this new engine type will be
 defined by you but in the middle of the values of the other engines.
 10. Implement a set of validations for the vehicles created. It means, a vehicle should
 have a valid model name (less than 30 characters, and just numbers and letters),
 a valid year (between 1990 and 2025), a valid price (between 20000000 COP and
 500000000 COP), and a valid chassis (A or B).


 You must deliver a technical report where a Class Diagram of your solution is pro
vided, also all related updated additional documentation; here it is recommended to think
 in components, define a diagram por each component where connections with other compo
nents will be absolutely clear. Also, you must write about technical concerns and decisions
 you make to create the architecture you are proposing; this includes SOLID implementa
tion analysis of your model, coupling, cohesion, and other software engineering principles.
 Finally, it is important you define why do you apply some patterns, and for any pattern
 you do not apply, you must explain why.


 
 You must update the code and provide a simple client interface with a menu to create
 vehicles, show all vehicles registered, and make searches by maximum speed, type of com
bustion, and range of years, showing vehicles and them specific information independently
 of the type, login users, subscribe users, and send newsletters