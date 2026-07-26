# Setup Guide

Follow these instructions to set up your GitHub profile repository perfectly.

## 1. Repository Creation
1. Create a new repository with a name exactly matching your GitHub username (`diwakar1215`).
2. Make sure it is **Public**.
3. Initialize it with a README (or just push this generated code).

## 2. GitHub Actions Permissions
To ensure the automated workflows (like the Snake animation) run correctly:
1. Go to your repository **Settings**.
2. Navigate to **Actions** -> **General**.
3. Under **Workflow permissions**, select **Read and write permissions**.
4. Click **Save**.

## 3. Customization
- **Images**: Replace the placeholder images in `assets/screenshots/` with actual screenshots of your projects.
- **Resume**: Replace `assets/Diwakar_Singh_Resume.pdf` with your actual resume.
- **Links**: Search the `README.md` for `mailto:contact@example.com` or `#` and replace them with your actual email and project links.

## 4. Trigger Workflows
1. Go to the **Actions** tab in your repository.
2. Select the **Generate Snake** workflow.
3. Click **Run workflow**. 
4. Once completed, a new branch `output` will be created containing the snake SVG, which the README uses!

For further customization, refer to [docs/customization.md](./docs/customization.md).
