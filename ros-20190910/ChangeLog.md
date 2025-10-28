2025-10-28 Version: 3.6.0
- Support API EnableServiceAccess.
- Support API EnableServices.
- Support API GetServiceAccess.
- Support API ListSummaries.


2025-08-20 Version: 3.5.7
- Update API PreviewStack: add request parameters UsePreviousParameters.


2025-06-04 Version: 3.5.6
- Update API CreateChangeSet: add request parameters TaintResources.
- Update API PreviewStack: add request parameters TaintResources.
- Update API UpdateStack: add request parameters TaintResources.


2025-05-22 Version: 3.5.5
- Update API GetServiceProvisions: add response parameters Body.ServiceProvisions.$.CommodityProvisions.


2025-04-27 Version: 3.5.4
- Generated python 2019-09-10 for ROS.

2025-04-18 Version: 3.5.3
- Update API GetTemplateParameterConstraints: add response parameters Body.ParameterConstraints.$.OriginalConstraints.$.PropertiesData.
- Update API GetTemplateParameterConstraints: add response parameters Body.ParameterConstraints.$.OriginalConstraints.$.RequestInfo.


2025-03-28 Version: 3.5.2
- Update API CreateChangeSet: add request parameters ResourceGroupId.
- Update API CreateChangeSet: add request parameters Tags.
- Update API GetChangeSet: add response parameters Body.ResourceGroupId.
- Update API GetChangeSet: add response parameters Body.Tags.
- Update API ListChangeSets: add response parameters Body.ChangeSets.$.ResourceGroupId.
- Update API ListChangeSets: add response parameters Body.ChangeSets.$.Tags.


2025-01-17 Version: 3.5.1
- Update API CreateStackInstances: add param DeploymentOptions.
- Update API GetTemplate: update response param.
- Update API GetTemplateParameterConstraints: update response param.
- Update API ListTemplates: add param Filters.
- Update API ListTemplates: update response param.
- Update API UpdateStackGroup: add param DeploymentOptions.


2024-11-20 Version: 3.5.0
- Support API ImportStacksToStackGroup.
- Update API CreateStackGroup: add param StackArn.


2024-08-09 Version: 3.4.3
- Generated python 2019-09-10 for ROS.

2024-08-08 Version: 3.4.2
- Update API UpdateTemplate: update response param.


2024-08-01 Version: 3.4.1
- Update API CreateTemplate: add param ValidationOptions.
- Update API UpdateTemplate: add param IsDraft.
- Update API UpdateTemplate: add param RotateStrategy.
- Update API UpdateTemplate: add param ValidationOptions.


2024-07-25 Version: 3.4.0
- Support API CreateAITask.
- Support API GetAITask.
- Support API ListAITaskEvents.
- Support API ListAITasks.


2024-07-25 Version: 3.4.0
- Support API CreateAITask.
- Support API GetAITask.
- Support API ListAITaskEvents.
- Support API ListAITasks.


2024-07-18 Version: 3.3.17
- Update API GetTemplateParameterConstraints: update response param.


2024-06-21 Version: 3.3.16
- Update API DeleteStack: add param Parallelism.


2024-06-17 Version: 3.3.15
- Update API CreateStackInstances: update param DeploymentTargets.


2024-05-10 Version: 3.3.14
- Update API GetStackGroup: update response param.
- Update API ListStackGroups: update response param.


2024-04-24 Version: 3.3.13
- Generated python 2019-09-10 for ROS.

2024-04-24 Version: 3.3.12
- Update API CreateTemplateScratch: update param SourceResources.
- Update API GetTemplateScratch: update response param.
- Update API UpdateStack: update param DisableRollback.


2024-03-22 Version: 3.3.11
- Update API CreateDiagnostic: add param Lang.
- Update API GetStack: update response param.
- Update API GetStackInstance: add param OutputOption.
- Update API GetStackInstance: update response param.


2024-02-29 Version: 3.3.10
- Update API GetStack: update response param.
- Update API GetStackInstance: add param OutputOption.
- Update API GetStackInstance: update response param.


2024-02-29 Version: 3.3.9
- Update API GetStack: update response param.
- Update API GetStackInstance: add param OutputOption.
- Update API GetStackInstance: update response param.


2024-02-21 Version: 3.3.8
- Update API GetStackInstance: add param OutputOption.
- Update API GetStackInstance: update response param.


2024-02-21 Version: 3.3.7
- Generated python 2019-09-10 for ROS.

2024-01-30 Version: 3.3.6
- Update API DeleteStackInstancesupdate DeploymentTargets param.


2024-01-12 Version: 3.3.5
- Generated python 2019-09-10 for ROS.

2024-01-11 Version: 3.3.4
- Generated python 2019-09-10 for ROS.

2024-01-11 Version: 3.3.3
- Adjust the parameter position of TemplateBody in CreateStack,UpdateStack,PreviewStack,CreateStackGroup,UpdateStackGroup,CreateChangeSet to adapt to large templates.

2024-01-10 Version: 3.3.2
- DeleteStackInstances supports specifying account ids in resource directory mode.

2023-10-19 Version: 3.3.1
- The input parameter SourceResources of CreateTemplateScratch has added RegionId, which only takes effect when TemplateScratchType is ArchitectureDetection.

2023-10-12 Version: 3.3.0
- Generated python 2019-09-10 for ROS.

2023-10-10 Version: 3.2.32
- Generated python 2019-09-10 for ROS.

2023-08-17 Version: 3.2.31
- Generated python 2019-09-10 for ROS.

2023-08-12 Version: 3.2.30
- Generated python 2019-09-10 for ROS.

2023-07-31 Version: 3.2.29
- UpdateStack supports parameter analysis for replacement update.
- UpdateStack supports DryRunOptions.
- ValidateTemplate supports UpdateInfoOptions.

2023-07-14 Version: 3.2.28
- GetStack returns StackOperationProgress and StackActionProgress in ResourceProgress if ShowResourceProgress is set to PercentageOnly.

2023-06-25 Version: 3.2.27
- GenerateTemplateByScratch adds a new input parameter TemplateType.

2023-05-18 Version: 3.2.26
- GetTemplateEstimateCost adds a new input parameter StackId, which is used for inquiry of updating scenarios.
- Added OrderIds output to GetStack interface.

2023-05-10 Version: 3.2.25
- Support resource type registration and module.

2023-04-13 Version: 3.2.24
- Added StartTime and EndTime to ListStacks to filter Stacks based on time range.
- CreateStack adds CreateOptions for specifying multiple creation options.

2023-03-30 Version: 3.2.23
- GetFeatureDetails supports ResourceImport and DriftDetection.
- DeleteStack supports DeleteOptions.

2023-03-28 Version: 3.2.22
- Move the TemplateBody parameter of ValidateTemplate to the request body to support larger template size.

2023-03-15 Version: 3.2.21
- Add GetTemplateRecommendParameters  interface to SDK.

2023-02-09 Version: 3.2.20
- A new PhysicsResourceId field is added to the Resources returned by the PreviewStack interface.
- Added StackId parameter to the GetTemplateParameterConstraints API.

2023-02-02 Version: 3.2.19
- UpdateStack supports DryRun and returns DryRunResult.
- ValidateTemplate returns UpdateInfo.
- GetFeatureDetails supports parameter constraint query function.
- Add API GetTemplateRecommendParameters.

2023-01-11 Version: 3.2.18
- Add API CancelStackOperation.

2022-12-08 Version: 3.2.17
- GenerateTemplatePolicy adds parameter OperationTypes.

2022-11-30 Version: 3.2.16
- ContinueCreateStack returns DryRunResult when DryRun is set to true.

2022-11-23 Version: 3.2.15
- The reponse of ValidateTemplate supports Outputs Label.
- Added ParametersOrder parameter to the GetTemplateParameterConstraints API.

2022-11-22 Version: 3.2.14
- The Tags parameter is supported in the ListStackGroups, ListTemplateScratches and CreateTemplateScratch API.

2022-10-28 Version: 3.2.13
- Add ApiForCreation in the return value ServiceProvisions-RoleProvision-Roles of GetServiceProvisions API.
- The Tags parameter is supported in the CreateTemplate and CreateStackGroup API.
- ListStackOperationRisks API support permission risk check when creating Stack.
- ContinueCreateStack support parameter RecreatingOptions.

2022-09-29 Version: 3.2.12
- Add IllegalValueByRules and IllegalValueByParameterConstraints to GetTemplateParameterConstraints output.
- Add Resources to ValidateTemplate output.

2022-09-08 Version: 3.2.11
- OperationInfo is added to the return value of GetStack and ListStacks.

2022-09-05 Version: 3.2.10
- Ros supports pre config.

2022-08-17 Version: 3.2.9
- GetFeatureDetail returns supported resource types for terraform risk check.

2022-07-21 Version: 3.2.8
- GetTemplateSummary support Parameters and ClientToken.

2022-07-13 Version: 3.2.7
- PreviewStack adds StackId and returns Action to support preview stack update.

2022-06-30 Version: 3.2.6
- ValidateTemplate returns ResourceTypes.
- GetStackResource supports ResourceAttributes.
- GetStack supports LogOption and returns ResourceLogs.

2022-06-09 Version: 3.2.5
- The parameter of GetStack, ListTemplates adds IncludeTags.
- The response of GetStack, ListTemplates adds Tags.

2022-05-19 Version: 3.2.4
- GetFeatureDetails supports ResourceCleaner.

2022-05-07 Version: 3.2.3
- Added diagnostic feature interface.

2022-04-25 Version: 3.2.2
- The Feature parameter of GetFeatureDetails is supported to be specified as TemplateScratch, which indicates the supported resource types for the template scratch.

2022-02-28 Version: 3.2.1
- The response of GetServiceProvisions adds DependentServiceNames.

2022-02-22 Version: 3.2.0
- The parameter of GetStack, GetTemplate, ListTemplates, ListTemplateVersions adds AcceptLanguage.
- The response of GetStack, GetTemplate adds Interface.
- The parameter of CreateStack, CreateChangeSet adds ServiceManaged.
- The response of GetStack adds ServiceManaged, ServiceName.
- The response of ListStacks adds ServiceManaged, ServiceName in Stacks.

2022-01-18 Version: 3.1.0
- Added EntityType to ListResourceTypes parameters.
- Added EntityType to GetResourceType return value.

2022-01-12 Version: 3.0.6
- GetFeatureDetails return value adds UpdateAllowedTransforms.

2022-01-05 Version: 3.0.5
- GetTemplate return value adds TemplateId, TemplateVersion, TemplateScratchId and TemplateURL.

2021-12-20 Version: 3.0.4
- CreateStack, PreviewStack and GetTemplateEstimateCost parameters supports specifing TemplateScratchRegionId.
- GetTemplateScratch return value adds StackProvision and UsageType in Stacks.
- GetTemplate return value adds ShareSource in Permissions.

2021-12-14 Version: 3.0.3
- Fix the issue that some parameters cannot be passed.

2021-12-07 Version: 3.0.2
- API GetStack supports Log for Terraform Stack.
- API GetChangeSet supports Log for Terraform Stack.
- API PreviewStack supports Log for Terraform Stack.

2021-11-30 Version: 3.0.1
- API GetStack supports Log for Terraform Stack.
- API GetChangeSet supports Log for Terraform Stack.
- API PreviewStack supports Log for Terraform Stack.

2021-11-22 Version: 3.0.0
- Add API GetServiceProvisions.
- Add API GetTemplateParameterConstraints.
- Add API GetFeatureDetails.
- CreateChangeSet supports Parallelism.

2021-09-23 Version: 2.1.3
- Terraform stack supports custom of parallelism.

2021-09-16 Version: 2.1.2
- Fixed the property AdministratorRoleName in GetStackGroupOperation  to AdministrationRoleName.

2021-09-03 Version: 2.1.1
- Fix type error of StackGroup and StackInstance parameters.

2021-09-03 Version: 2.1.0
- StackGroup supports specify resource folder to deploy StackInstances.
- StackGroup supports SERVICE_MANAGED and SELF_MANAGED permission models.

2021-08-27 Version: 2.0.6
- Support ClientToken for ValidateTemplate.

2021-07-20 Version: 2.0.5
- GetStack supports resource progress.
- ValidateTemplate supports Outputs.

2021-03-31 Version: 2.0.4
- Generated python 2019-09-10 for ROS.

2021-01-22 Version: 2.0.3
- Generated python 2019-09-10 for ROS.

2021-01-22 Version: 1.3.0
- Generated python 2019-09-10 for ROS.

2021-01-21 Version: 1.2.2
- Generated python 2019-09-10 for ROS.

2021-01-21 Version: 1.2.1
- The creation and update APIs of the stack supports specifing tags, and the query and list APIs supports obtaining tags.

2021-01-20 Version: 2.0.2
- AMP Version Change.

2021-01-20 Version: 2.0.1
- AMP Version Change.

2020-12-30 Version: 2.0.0
- AMP Version Change.

2020-12-30 Version: 2.0.0
- AMP Version Change.

2020-12-17 Version: 1.2.0
- Support template version.
- Support to share template.
- Stack and StackGroup support TemplateId and TemplateVersion.
- Add GenerateTemplatePolicy which can generate RAM policy by template.

