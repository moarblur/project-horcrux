# Project Horcrux
EchoVault is conceived as a privacy-first digital platform dedicated to the secure capture, encryption, and controlled sharing of personal thoughts, memories, secrets, or reflections – termed "Horcruxes."
---

**[First Draft] Project Document: EchoVault**

**Tagline:** Seal your memories, share on your terms.

-----

### 📝 **Project Naming & Branding Note**

"EchoVault" is the current working title. A final name and associated branding guidelines will be developed and documented separately as the project matures. Community input will be welcomed during that process.

-----

### 🚀 Project Overview

EchoVault is conceived as a privacy-first digital platform dedicated to the secure capture, encryption, and controlled sharing of personal thoughts, memories, secrets, or reflections – termed "Horcruxes." Each Horcrux is designed as a context-rich, encrypted payload. Users retain absolute control, deciding precisely when, with whom, and for how long this sensitive information is shared, with the ability to revoke access at any time.

The platform aims to serve individuals who prioritize emotional transparency and connection but refuse to compromise on personal privacy, trust, or control over their digital narrative. EchoVault provides an immutable record of disclosures, ensuring users always know what was shared, with whom, and the context surrounding it. Our core principle is **zero-knowledge encryption**, meaning EchoVault servers never have access to the unencrypted content of your Horcruxes.

-----

### 🏗️ Tech Stack & Architecture

  * **Frontend**: React (with Tailwind CSS) - Chosen for its component-based architecture, enabling a responsive and maintainable UI.
  * **Backend**: Flask (Python) - Selected for its simplicity, flexibility as a microservice framework, and the rich Python ecosystem for cryptography and web tasks. Handles API requests, metadata storage, and notification orchestration.
  * **Storage**:
      * Metadata & Encrypted Payloads: MongoDB (production) or SQLite (local development) - Chosen for flexible schema handling. Encrypted content is stored as ciphertext blobs.
      * Future (V2+): Potential integration with IPFS for decentralized storage options.
  * **Encryption**:
      * Client-Side: WebCrypto API in the browser for robust, standard-based zero-knowledge encryption/decryption using user-derived keys (passphrases).
      * Server-Side: PyNaCl library for managing any necessary server-side symmetric key operations securely (e.g., related to secure links, *not* user content).
  * **Notifications**: SMTP for email notifications and WebSockets for real-time in-app alerts.
  * **CI/CD**: GitHub Actions for automated linting, testing, and potentially deployment pipelines.
  * **Deployment**: Docker-compose for easy local development setup; a Kubernetes Helm chart is planned for scalable production deployments.

**High‑Level Data Flow:**

1.  User composes a Horcrux in the browser.
2.  Content is encrypted client-side using the user's passphrase (key is never sent to the server).
3.  Encrypted ciphertext and non-sensitive metadata (title, tags, recipient info) are sent to the backend API.
4.  Backend stores ciphertext and metadata in the database.
5.  Backend generates secure sharing links or triggers notifications (email/WebSocket) for recipients.
6.  Recipient accesses the link/notification.
7.  Backend serves the ciphertext to the recipient's client upon successful authentication/authorization.
8.  Recipient's browser decrypts the content locally using a shared secret or mechanism (details TBD, could involve passphrase exchange out-of-band or other E2EE methods).
9.  The backend records access and other relevant events in an immutable audit log.

-----

### 🎯 Core MVP Features (V1.0)

1.  **Horcrux Creation & Encryption:**
      * Interface to compose a title, main body text, and optional tags (e.g., emotion, event type, version).
      * Client-side, zero-knowledge encryption tied to a user-specific passphrase before any data leaves the browser.
2.  **Recipient Assignment & Secure Delivery:**
      * Ability to assign recipients via email address or platform username.
      * Generation of secure, unique links for accessing the encrypted Horcrux.
      * Option for in-app notifications (via WebSockets) or email alerts to recipients.
3.  **Access Audit & Notifications:**
      * Immutable, real-time logs recording key events: Horcrux creation, sharing, first view attempt (timestamp, recipient ID, action).
      * Optional notification (email or in-app) sent to the creator upon the first successful access by a recipient.
4.  **Revocation & Expiry Controls:**
      * Manual "Revoke Access" button allowing creators to immediately invalidate sharing links for specific recipients or all recipients of a Horcrux.
      * Option to set an expiry date/time *or* a maximum view count, after which the Horcrux becomes automatically inaccessible.

-----

### 🗺️ Nice-to-Have Features (V2.0+)

  * **Dead-Man Switch:** Automated release of designated Horcruxes to pre-assigned recipients if the creator's account shows inactivity for a configurable period.
  * **Relationship Graph:** A visual representation showing which Horcruxes (or fragments) have been shared with which contacts.
  * **Mobile Applications:** Native iOS/Android apps with features like push notifications and biometric authentication (Fingerprint/Face ID) for enhanced security and usability.
  * **Blockchain Anchoring (Optional):** Timestamping Horcrux metadata hashes on a public blockchain (e.g., Bitcoin, Ethereum L2) for proof-of-existence and tamper evidence, while keeping encrypted data securely off-chain.
  * **IPFS Integration:** Option to store encrypted Horcrux payloads on the InterPlanetary File System for decentralized persistence.

-----

### 📋 Project Roadmap

| Phase     | Focus                                                                       | Estimated Timeline |
| --------- | --------------------------------------------------------------------------- | ------------------ |
| **Alpha** | Core UI/UX mockups, foundational frontend components, client-side encryption logic, local storage mocks. | Month 1            |
| **Beta** | Backend API development, database integration (MongoDB/SQLite), user authentication, basic recipient sharing flow, initial audit logging. | Month 2            |
| **Gamma** | Implement revocation logic, expiry policies, email/WebSocket notifications, Docker setup refinement, basic testing suite. | Month 3            |
| **V1.0** | Public launch readiness: Core MVP features complete, documentation (user & contributor), UX polishing based on internal feedback, security review. | Month 4            |
| **V2.0+** | Development of post-MVP features (Dead-Man Switch, Relationship Graph, Mobile Apps, Blockchain/IPFS integration) based on priority and community feedback. | Month 6+           |

-----

### 👥 Roles & Governance

This is an open-source project welcoming collaboration.

  * **Project Owner (You):** Defines the initial vision, makes final decisions on core architecture and direction, stewards the overall project health.
  * **Sr. Maintainer / Architect:** Experienced developers responsible for reviewing core feature PRs, maintaining architectural integrity, guiding technical decisions, and mentoring contributors. *To apply, please email [moarblur.j8fo9@aleeas.com](mailto:moarblur.j8fo9@aleeas.com) with your background, relevant experience (especially in security, cryptography, web development), and motivation for joining.*
  * **Contributors:** Anyone interested in improving EchoVault\! Contributions can include coding new features, fixing bugs, writing tests, improving documentation, or refining the UI/UX. Look for issues tagged `good-first-issue` or `help-wanted`.
  * **Consultants / Auditors:** We actively encourage experts in security, cryptography, user experience, and privacy law to review our design, architecture, and implementation. Please use the `security` or `design` issue templates or reach out directly.
  *   **Note:** We can additionally or primarily make a separate markdown document (contributor-applications.md) so interested folks can submit applications via a merge request.

**Code of Conduct:** We enforce a strict **Code of Conduct** ([CODE\_OF\_CONDUCT.md](../CODE_OF_CONDUCT.md)) to ensure a respectful, welcoming, and productive environment for everyone. Intolerance or harassment will not be permitted.

See [../SECURITY.md](../SECURITY.md) for our security disclosure process.
-----

### 🤝 Contributing & Collaboration

We appreciate all contributions\! Here’s how to get involved:

1.  **Find an Issue:** Browse the issue tracker. Pick an existing issue or open a new one to discuss your proposed change (bug fix, feature, improvement). Use the provided **Issue Templates**.
2.  **Fork & Clone:** Fork the repository to your GitHub account and clone it locally.
    ```bash
    git clone https://github.com/moarblur/project-horcrux.git
    cd project-horcrux
    ```
3.  **Create a Branch:** Create a descriptive branch for your work.
    ```bash
    git checkout -b feature/your-descriptive-feature-name
    ```
4.  **Develop & Test:** Implement your changes. **Crucially, write tests** for any new functionality or bug fixes. Ensure existing tests pass. Adhere to coding standards (PEP8 for Python, ESLint for React).
5.  **Document:** Update any relevant documentation (README, technical docs, user guides).
6.  **Submit a Pull Request (PR):** Push your branch to your fork and open a PR against the main EchoVault repository.
      * Link the PR to the relevant issue(s).
      * Provide a clear description of the changes, including *why* they were made. Include screenshots or mockups if UI changes are involved.
      * Mark the PR as "Draft" if it's work-in-progress and you're seeking early feedback.
7.  **Review:** Maintainers will review PRs, typically on a weekly cadence. Be prepared to discuss your changes and make adjustments based on feedback.

**Issue Templates:**

  * `good-first-issue`: Great starting points for newcomers.
  * `help-wanted`: Tasks needing contributor assistance.
  * `feature-request`: Proposing new functionality.
  * `bug`: Reporting errors or unexpected behavior.
  * `security`: **Responsible disclosure** of security vulnerabilities (see SECURITY.md for process).
  * `design`: Discussions related to UI/UX or architectural choices.

-----

### 🛠️ Getting Started (Local Development)

**Prerequisites:**

  * Node.js (v16 or later recommended)
  * Python (v3.9 or later recommended)
  * pip (Python package installer)
  * Git
  * Docker & Docker Compose (Optional, but recommended for easy setup)

**Steps:**

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/moarblur/project-horcrux.git
    cd project-horcrux
    ```
2.  **Backend Setup:**
    ```bash
    cd backend
    python3 -m venv venv          # Create a virtual environment
    source venv/bin/activate      # Activate (Linux/macOS)
    # or `.\venv\Scripts\activate` # Activate (Windows)
    pip install -r requirements.txt # Install backend dependencies
    # Copy .env.example to .env and fill in necessary values (DB connection, secrets)
    cp .env.example .env
    # Edit .env with your configuration
    flask run                     # Start the backend server
    ```
3.  **Frontend Setup:**
    ```bash
    cd ../frontend
    npm install                   # Install frontend dependencies
    npm start                     # Start the frontend dev server
    ```
4.  **Docker Setup (Alternative):**
      * Ensure Docker and Docker Compose are installed.
      * From the project root directory (`echovault`):
        ```bash
        # Copy backend/.env.example to backend/.env and configure it first
        cp backend/.env.example backend/.env
        # Edit backend/.env
        docker-compose up --build   # Build and start containers
        ```
      * This will typically start the frontend, backend, and a database container (e.g., MongoDB).

**Environment Variables:** Check the `.env.example` files in both `frontend` and `backend` directories for required configuration (API URLs, database credentials, secret keys, etc.). Create `.env` files from these examples for your local setup.

-----

### 🎨 Initial Wireframes & Sketches (Placeholder)

*Detailed designs and prototypes will be maintained in a dedicated tool (e.g., Figma).*

```
+--------------------------+      +-----------------------------+      +--------------------------+
| Create Horcrux           |      | Assign & Share Horcrux #ID  |      | Dashboard / Vault View   |
| ------------------------ |      | --------------------------- |      | ------------------------ |
| Title: [______________]  |      | Add Recipient (Email/User): |      | My Horcruxes:            |
| Body: [TextArea_______]  |      | [___________________] [Add] |      | - Secret Plan (Shared: 2)|
| Tags: [tag1, tag2 ] [x] |      | -> user@example.com [x]     |      |   [Details] [Revoke All] |
| Passphrase: [********]   |      | -> another_user     [x]     |      | - Old Memory (Shared: 1) |
| [ Seal Horcrux ]         |      |                             |      |   [Details] [Revoke...]  |
+--------------------------+      | Expiry: [Date Picker]       |      | - Draft Idea (Private)   |
                              | Max Views: [___] (optional) |      |   [Edit] [Share]         |
                              | [ Generate Secure Links ]   |      +--------------------------+
                              +-----------------------------+

+--------------------------------+
| View Horcrux (Recipient View)  |
| ------------------------------ |
| From: [Creator Name/Anon]      |
| Title: [Horcrux Title]         |
| Body:                          |
| [ Decrypted Content Here ]     |
|                                |
| Received: [Timestamp]          |
| Expires: [Date or Never]       |
+--------------------------------+
```

-----

### 📑 License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/moarblur/project-horcrux/blob/main/LICENSE) file for full details. License subject to change in future iterations.

-----

> "Some memories are whispered, not shouted. Keep them safe, share them wisely."
