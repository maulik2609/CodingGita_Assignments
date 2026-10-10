# Section A: Short Answer Questions (1 Mark each)

**Q1. What is JavaScript?**

**Answer:** JavaScript is a lightweight, interpreted (or JIT-compiled) high-level programming language used to make web pages interactive and dynamic. It runs in the browser and also outside it (via Node.js).

---

**Q2. Who created JavaScript and in which year?**

**Answer:** JavaScript was created by **Brendan Eich** in **1995**, while he was working at Netscape.

---

**Q3. What was the original name of JavaScript?**

**Answer:** Its original name was **Mocha**. It was later renamed **LiveScript**, and finally **JavaScript**.

---

**Q4. Is JavaScript the same as Java? Give one major difference.**

**Answer:** No, they are completely different languages. Java is a statically-typed, compiled language mainly used for enterprise and Android apps. JavaScript is a dynamically-typed, interpreted language mainly used for web development.

---

**Q5. What does it mean when we say JavaScript is a high-level programming language?**

**Answer:** A high-level language is closer to human language and far from machine code. You don't need to manage memory manually or write binary/assembly. The engine handles those low-level details for you.

---

**Q6. Is JavaScript a compiled language or an interpreted language? Explain briefly.**

**Answer:** JavaScript is mainly an **interpreted** language: the JS engine reads and executes code line by line. However, modern engines like V8 use **JIT (Just-In-Time) compilation**, converting code to machine code at runtime for speed. So it is traditionally classified as interpreted, though technically it is a mix.

---

**Q7. Name the JavaScript engines used by the following browsers.**

**Answer:**
- Google Chrome → **V8**
- Mozilla Firefox → **SpiderMonkey**
- Apple Safari → **JavaScriptCore (Nitro)**

---

**Q8. What is Dynamic Typing in JavaScript?**

**Answer:** Dynamic typing means you don't declare a variable's data type explicitly. The type is decided automatically at runtime, and a variable can hold different types of values at different times.

```javascript
let x = 10;      // x is a number
x = "hello";     // now x is a string, no error
```

---

**Q9. What is the main difference between a static website and a dynamic website?**

**Answer:**
- **Static website:** Content is fixed and the same for every user. It is built with plain HTML/CSS and changes only when the developer edits the code.
- **Dynamic website:** Content changes based on user interaction, database data, or server response (e.g., a logged-in dashboard, a social media feed).

---

**Q10. Name the three pillars of Front-end Web Development and write one line about each.**

**Answer:**
1. **HTML**: provides the structure/skeleton of the webpage.
2. **CSS**: handles styling and visual presentation (colors, layout, fonts).
3. **JavaScript**: adds behavior and interactivity (click events, animations, logic).

---

**Q11. What is the difference between Frontend and Backend?**

**Answer:**
- **Frontend:** Everything the user sees and interacts with directly in the browser (UI, buttons, forms).
- **Backend:** The server-side logic, database, and infrastructure that processes requests and sends data to the frontend.

---

**Q12. What is Node.js?**

**Answer:** Node.js is a **runtime environment** that lets you run JavaScript **outside the browser** (e.g., on a server). It is built on Chrome's V8 engine and is used for backend development, file handling, servers, etc.

---

**Q13. Explain ECMAScript. What is its relation with JavaScript?**

**Answer:** ECMAScript (ES) is the **standard/specification** that JavaScript is based on. JavaScript is an **implementation** of ECMAScript. Think of ECMAScript as the rulebook and JavaScript as a language that follows those rules. Versions like ES5, ES6/ES2015


  # Section B: True or False
(Write True or False. If False, correct the statement.)

**1. JavaScript is a statically typed language.**

**Answer: False.** JavaScript is a **dynamically** typed language.

---

**2. JavaScript can only run inside the browser.**

**Answer: False.** JavaScript can also run outside the browser, for example using **Node.js**.

---

**3. HTML is responsible for the behaviour of a webpage.**

**Answer: False.** HTML is responsible for the **structure** of a webpage. Behaviour is handled by **JavaScript**.

---

**4. Node.js allows JavaScript to run outside the browser.**

**Answer: True.**

---

**5. JavaScript is case-insensitive.**

**Answer: False.** JavaScript is **case-sensitive**.

---

**6. `let name` and `let Name` are the same variable.**

**Answer: False.** They are **different** variables because JavaScript is case-sensitive.

---

**7. ECMAScript is a programming language.**

**Answer: False.** ECMAScript is a **specification/standard**, not a programming language itself.

---

**8. React, Angular, and Vue.js are used for Backend development.**

**Answer: False.** React, Angular, and Vue.js are used for **Frontend** development.

  # Section C: Fill in the Blanks

**1. JavaScript was created by ______________ in the year ______________.**

**Answer:** JavaScript was created by **Brendan Eich** in the year **1995**.

---

**2. The three technologies used in Front-end development are __________, __________, and __________.**

**Answer:** The three technologies used in Front-end development are **HTML**, **CSS**, and **JavaScript**.

---

**3. JavaScript engines: Chrome uses __________, Firefox uses __________.**

**Answer:** Chrome uses **V8**, Firefox uses **SpiderMonkey**.

---

**4. In the restaurant analogy: Customer = __________, Waiter = __________, Chef = __________.**

**Answer:** Customer = **User/Browser (Frontend)**, Waiter = **Server/API**, Chef = **Backend/Database**.

---

**5. JavaScript file extension is __________.**

**Answer:** The JavaScript file extension is **.js**.

  # Section D: Conceptual Questions (2 Marks each)

**Q14. Differentiate between a static website and a dynamic website. Give one real-world example of each.**

**Answer:** A **static website** shows the same fixed content to every visitor and doesn't interact with a database. Example: a simple portfolio page with hardcoded HTML.

A **dynamic website** generates or changes content based on user input, time, or database queries. Example: Instagram, where your feed differs from everyone else's and updates constantly.

---

**Q15. Explain any two features of JavaScript that make it suitable for creating interactive web pages.**

**Answer:**
1. **Event handling:** JS can detect user actions like clicks, key presses, or mouse movement and respond instantly (e.g., showing a menu on click).
2. **DOM manipulation:** JS can change HTML content, styles, and structure without reloading the page (e.g., updating a cart count when you add an item).

---

**Q16. List any four areas (apart from web browsers) where JavaScript is used today. Mention one popular framework/library for each.**

**Answer:**
1. **Backend development:** Node.js
2. **Mobile app development:** React Native
3. **Desktop app development:** Electron.js
4. **AI/Machine Learning:** TensorFlow.js

---

**Q17. What is the difference between writing JavaScript code inside an HTML file using the `<script>` tag and in an external `.js` file? Mention two advantages of using an external JavaScript file.**

**Answer:**
- **Inside HTML (`<script>` tag):** The JS code is written directly inside the HTML file.
- **External `.js` file:** The JS code is written in a separate file and linked using `<script src="file.js"></script>`.

Two advantages of an external file:
1. **Reusability:** the same JS file can be linked to multiple HTML pages.
2. **Better maintainability:** HTML (structure) and JS (logic) stay separate, making code cleaner and easier to debug and update.

---

**Q18. Explain the difference between Frontend and Backend using the restaurant analogy in your own words.**

**Answer:** In a restaurant, **you (the customer)** are like the frontend. You see the menu and place an order, just as a user interacts with a website's interface. The **waiter** is like the backend server. They take your request to the kitchen and bring the response back, like an API relaying requests between the browser and the database. The **chef** is like the database, which prepares and stores the "data" (food) that gets delivered back to you.

---

**Q19. Why should a beginner learn JavaScript? Write at least 4 points.**

**Answer:**
1. It is the **only language browsers understand natively**, so it is essential for web development.
2. It has **huge demand** in the job market for frontend, backend, and full-stack roles.
3. It has a **massive ecosystem**: React, Angular, Vue, and Node.js are all JS-based.
4. It is **beginner-friendly**: you only need a browser to start, with no complex setup.

  # Section E: Code-Based Questions (3 Marks each)

**Q20. Predict the output of the following code and explain why:**

```javascript
let value = 25;
console.log(typeof value);
value = "JavaScript";
console.log(typeof value);
value = false;
console.log(typeof value);
```

**Answer:**

Output:

```
number
string
boolean
```

Explanation: JavaScript is dynamically typed, so `typeof` returns the type of the **current value** stored in the variable at that moment. As `value` is reassigned from a number (`25`) to a string (`"JavaScript"`) to a boolean (`false`), its type changes each time.

---

**Q21. Write a simple HTML + JavaScript program that displays an alert box with the message "Welcome to JavaScript!" when a button is clicked.**

**Answer:**

```html
<!DOCTYPE html>
<html>
<head>
  <title>Alert Example</title>
</head>
<body>
  <button onclick="showAlert()">Click Me</button>

  <script>
    function showAlert() {
      alert("Welcome to JavaScript!");
    }
  </script>
</body>
</html>
```

---

**Q22. Write JavaScript code to demonstrate event-driven programming. When a user clicks a button with id "myBtn", the text of a paragraph with id "demo" should change to "Button was clicked!".**

**Answer:**

```html
<!DOCTYPE html>
<html>
<head>
  <title>Event Driven Example</title>
</head>
<body>
  <button id="myBtn">Click Me</button>
  <p id="demo">This text will change.</p>

  <script>
    document.getElementById("myBtn").addEventListener("click", function () {
      document.getElementById("demo").textContent = "Button was clicked!";
    });
  </script>
</body>
</html>
```
# Section F: Practical / Application Based (5 Marks)

**Q23. Create a complete web page (HTML + JavaScript) that includes the following:**

1. A heading: "My First JavaScript Page"
2. A button labeled "Click Me"
3. When the button is clicked:
   - Show an alert: "Hello, B.Tech Student!"
   - Change the background color of the page to light blue
4. Also print "JavaScript is running successfully!" in the browser console.

**Answer:**

```html
<!DOCTYPE html>
<html>
<head>
  <title>My First JavaScript Page</title>
</head>
<body>
  <h1>My First JavaScript Page</h1>
  <button id="actionBtn">Click Me</button>

  <script>
    document.getElementById("actionBtn").addEventListener("click", function () {
      alert("Hello, B.Tech Student!");
      document.body.style.backgroundColor = "lightblue";
      console.log("JavaScript is running successfully!");
    });
  </script>
</body>
</html>
```

How to run: save the code as `index.html`, open it with VS Code Live Server (or double-click it), and click the button. Open the browser console (F12) to see the console message.

  # Section G: Higher Order Thinking (Bonus - 3 Marks)

**Q24. JavaScript was originally created only for browsers. Today it is used in frontend, backend, mobile apps, desktop apps, and even AI/ML. In your own words, explain why JavaScript became so popular and multipurpose. Mention the role of Node.js and ECMAScript updates in this growth.**

**Answer:**

JavaScript became popular and multipurpose mainly because of two things: **Node.js** and **ECMAScript updates**.

Before Node.js, JavaScript could only run inside browsers, which limited it to frontend tasks. Node.js changed that by letting JavaScript run on servers. Developers could now use **one language for both frontend and backend**, which simplified full-stack development and led to wide adoption for backend APIs, real-time apps, and developer tooling.

At the same time, **ECMAScript updates** (like ES6/2015 and later) added modern features such as arrow functions, classes, promises, async/await, and modules. These made JavaScript more powerful, readable, and capable of handling complex applications. This steady evolution kept JavaScript relevant and allowed frameworks and tools like React, Angular, Vue, React Native, Electron, and TensorFlow.js to be built on top of it, taking it into mobile, desktop, and AI. This is how a browser scripting language became a multipurpose ecosystem.

  



Explanation: The code waits for a `click` event on the button and runs the function only when that event happens. This is event-driven programming.

  
