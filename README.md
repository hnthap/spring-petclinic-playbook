# spring-petclinic-playbook

## Setting up

1. Define these secrets using Ansible Vault (use a placeholder value for both the SonarQube token `vault_sonar_token` and the Nexus password `vault_nexus_password`):
  ```yaml
  # Run: ansible-vault create group_vars/all/vault.yml

  vault_sonar_db_password: "CHANGE_ME_STRONG_PASSWORD"
  vault_nexus_username: "admin"
  vault_slack_token: "TOKEN"
  vault_nexus_password: "PENDING"
  vault_sonar_token: "PENDING"
  vault_azure_ssh_key: "CHANGE_ME"

  # To acquire the SSH key, run:
  #
  #   cat ~/.ssh/id_25519
  #
  # Then copy and paste the text in place of "CHANGE_ME", for example:
  #
  #   vault_azure_ssh_key: |
  #     -----BEGIN OPENSSH PRIVATE KEY-----
  #     (paste your exact key contents here)
  #     (make sure all lines are indented identically)
  #     -----END OPENSSH PRIVATE KEY-----
  ```
2. Execute the playbook:
  ```bash
  # You can define CONTROL_IP_ADDR and TARGET_IP_ADDR to override the default
  # IP addresses in inventory.py

  ansible-playbook -i inventory.py infra.yml -K --ask-vault-pass
  ```
3. Retrieve the default Nexus admin password from the target node:
  ```bash
  ssh <ansible_user>@<target_ip> "sudo cat /opt/sonatype-work/nexus3/admin.password"
  ```
4. Log into the SonarQube UI (`http://<target_ip>:9000`), force the password change, and generate the user token. Copy the token.
5. Log into the Nexus UI (`http://<target_ip>:8081`) with the username `admin` and the temporary password from Step 3, then follow the prompt to set a new, permanent password. Copy this password.
6. Run Ansible Vault again (`ansible-vault edit group_vars/all/vault.yml`) and replace the placeholders for both `vault_sonar_token` and `vault_nexus_password` with the actual values obtained in Steps 4 and 5.
7. Execute the playbook again.
