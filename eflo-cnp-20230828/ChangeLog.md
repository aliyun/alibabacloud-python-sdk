2025-05-15 Version: 2.0.0
- Support API DeleteExperimentPlan.
- Support API GetExperimentPlanTemplate.
- Support API ListTagResources.
- Support API TagResources.
- Support API UntagResources.
- Support API UpdateExperimentPlan.
- Support API UpdateExperimentPlanTemplate.
- Update API ChangeResourceGroup: add request parameters RegionId.
- Update API CreateExperimentPlan: add request parameters PlanTemplateName.
- Update API CreateExperimentPlan: add request parameters Tag.
- Update API CreateExperimentPlanTemplate: add response parameters Body.Data.TemplateCode.
- Update API CreateResource: delete request parameters ClusterType.
- Update API CreateResource: delete request parameters ResourceType.
- Update API DeleteExperiment: add request parameters ResourceGroupId.
- Update API GetExperiment: add request parameters ResourceGroupId.
- Update API GetExperimentPlan: add response parameters Body.Data.Tags.
- Update API GetExperimentResultData: add request parameters ResourceGroupId.
- Update API GetResource: delete response parameters Body.Data.ResourceName.
- Update API ListExperimentPlanTemplates: add response parameters Body.Data.$.TemplateCode.
- Update API ListExperimentPlanTemplates: add response parameters Body.Data.$.TemplatePipelineParam.$.EnvParams.CudaVersion.
- Update API ListExperimentPlanTemplates: add response parameters Body.Data.$.TemplatePipelineParam.$.EnvParams.GpuDriverVersion.
- Update API ListExperimentPlanTemplates: add response parameters Body.Data.$.TemplatePipelineParam.$.EnvParams.NCCLVersion.
- Update API ListExperimentPlanTemplates: add response parameters Body.Data.$.TemplatePipelineParam.$.EnvParams.PyTorchVersion.
- Update API ListExperimentPlans: add request parameters ResourceId.
- Update API ListExperimentPlans: add request parameters Tag.
- Update API ListExperimentPlans: add request parameters TemplateId.
- Update API ListExperimentPlans: add response parameters Body.Data.$.ResourceId.
- Update API ListExperimentPlans: add response parameters Body.Data.$.Tags.
- Update API ListExperiments: add request parameters ResourceGroupId.
- Update API StopExperiment: add request parameters ResourceGroupId.


2025-01-03 Version: 1.0.0
- Generated python 2023-08-28 for eflo-cnp.

