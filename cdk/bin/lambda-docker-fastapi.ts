#!/usr/bin/env node
import "source-map-support/register";
import * as cdk from "aws-cdk-lib";
import { CdkLambdaDockerFastapiStack } from "../lib/lambda-docker-fastapi";

const app = new cdk.App();
new CdkLambdaDockerFastapiStack(app, "CdkLambdaDockerFastapiStack", {});
