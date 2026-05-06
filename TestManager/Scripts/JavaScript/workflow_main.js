import 'dotenv/config';
import { Octokit } from "octokit";

const octokit = new Octokit({
    auth: process.env.GITHUB_AUTH_TOKEN
});

async function runWorkflow() {
    try {
        const resp = await octokit.request('POST /repos/{owner}/{repo}/actions/workflows/{workflow_id}/dispatches', {
            owner: 'dominic-anderson',
            repo: 'Test-Manager',
            workflow_id: 'main.yml',
            ref: 'main'
        });
        console.log('Dispatch response:', resp.status, resp.data);
    } catch (err) {
        console.error('Dispatch failed:', err.message);
        if (err.response) console.error('API error details:', err.response.data);
        process.exitCode = 1;
    }
}

runWorkflow();