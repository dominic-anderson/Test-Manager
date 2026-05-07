import 'dotenv/config';
import { Octokit, RequestError } from "octokit";

const octokit = new Octokit({
    auth: process.env.GITHUB_AUTH_TOKEN
});

async function runWorkflow() {
    try {
        const resp = await octokit.request('POST /repos/{owner}/{repo}/actions/workflows/{workflow_id}/dispatches', {
            owner: 'dominic-anderson',
            repo: 'Test-Manager',
            workflow_id: `${process.argv[3]}.yml`,
            ref: `${process.argv[3]}`
        });
        console.log('Dispatch response:', resp.status, resp.data);
    } catch (error) {
        if (error instanceof RequestError) {
            console.error('Dispatch failed:', error.message);
            if (error.response) console.error('API error details:', error.response.data);
        } else {
            console.error('Unexpected error:', error);
        }
        process.exitCode = 1;
    }
}

runWorkflow();