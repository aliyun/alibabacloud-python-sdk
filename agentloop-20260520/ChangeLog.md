2026-10-10 Version: 2.3.9
- Update API CreateContextStore: add request parameters body.config.audit.
- Update API CreateContextStore: add request parameters body.config.extractionPolicy.
- Update API CreateContextStore: add request parameters body.config.scopePolicy.
- Update API CreateContextStore: add request parameters body.config.storagePolicy.
- Update API CreateContextStore: add request parameters body.config.source.dataset.
- Update API CreateContextStore: add request parameters body.config.source.trajectory.
- Update API CreateContextStore: add request parameters body.config.source.type.
- Update API CreateContextStore: add response parameters Body.strategyVersion.
- Update API DeleteContextStore: add request parameters deleteOutputDataset.
- Update API GetContextStore: add response parameters Body.config.audit.
- Update API GetContextStore: add response parameters Body.config.extractionPolicy.
- Update API GetContextStore: add response parameters Body.config.innerSource.
- Update API GetContextStore: add response parameters Body.config.observability.
- Update API GetContextStore: add response parameters Body.config.outputDataset.
- Update API GetContextStore: add response parameters Body.config.scopePolicy.
- Update API GetContextStore: add response parameters Body.config.sourceStatus.
- Update API GetContextStore: add response parameters Body.config.storagePolicy.
- Update API GetContextStore: add response parameters Body.config.strategyVersion.
- Update API GetContextStore: add response parameters Body.config.source.dataset.
- Update API GetContextStore: add response parameters Body.config.source.trajectory.
- Update API GetContextStore: add response parameters Body.config.source.type.
- Update API ListContextStores: add request parameters sourceType.
- Update API ListContextStores: add response parameters Body.results.$.sourceType.
- Update API ListContextStores: add response parameters Body.results.$.storageMode.
- Update API SearchContext: add request parameters body.includeInactive.
- Update API SearchContext: add request parameters body.scope.
- Update API SearchContext: add response parameters Body.auditStatus.
- Update API SearchContext: add response parameters Body.recallEventId.
- Update API UpdateContextStore: add request parameters body.changeNote.
- Update API UpdateContextStore: add request parameters body.config.audit.
- Update API UpdateContextStore: add request parameters body.config.extractionPolicy.
- Update API UpdateContextStore: add request parameters body.config.scopePolicy.
- Update API UpdateContextStore: add request parameters body.config.storagePolicy.
- Update API UpdateContextStore: add request parameters body.config.source.dataset.
- Update API UpdateContextStore: add request parameters body.config.source.trajectory.
- Update API UpdateContextStore: add response parameters Body.strategyVersion.


2026-10-09 Version: 2.3.8
- Update API CreatePipeline: add request parameters body.executePolicy.continuous.
- Update API CreatePipeline: add request parameters body.source.trajectory.
- Update API GetPipeline: add response parameters Body.scheduleType.
- Update API GetPipeline: add response parameters Body.executePolicy.continuous.
- Update API GetPipeline: add response parameters Body.source.trajectory.
- Update API ListPipelines: add response parameters Body.pipelines.$.executePolicy.continuous.
- Update API ListPipelines: add response parameters Body.pipelines.$.source.inputFields.
- Update API ListPipelines: add response parameters Body.pipelines.$.source.trajectory.
- Update API PreviewPipeline: add request parameters body.source.trajectory.
- Update API PreviewPipeline: add response parameters Body.meta.schema.
- Update API UpdatePipeline: add request parameters body.executePolicy.continuous.
- Update API UpdatePipeline: add request parameters body.source.trajectory.


2026-09-21 Version: 2.3.7
- Update API UpdateDataset: add request parameters body.renames.


2026-09-14 Version: 2.3.5
- Update API ListPipelines: add request parameters sinkName.
- Update API ListPipelines: add response parameters Body.pipelines.$.sink.
- Update API ListPipelines: add response parameters Body.pipelines.$.source.


2026-08-31 Version: 2.3.3
- Update API CreatePipeline: add request parameters body.sink.condition.
- Update API CreatePipeline: add request parameters body.source.dataset.
- Update API CreatePipeline: add request parameters body.source.inputFields.
- Update API GetPipeline: add response parameters Body.sink.condition.
- Update API GetPipeline: add response parameters Body.source.dataset.
- Update API GetPipeline: add response parameters Body.source.inputFields.
- Update API PreviewPipeline: add request parameters body.source.dataset.
- Update API PreviewPipeline: add request parameters body.source.inputFields.
- Update API UpdatePipeline: add request parameters body.sink.condition.
- Update API UpdatePipeline: add request parameters body.source.dataset.
- Update API UpdatePipeline: add request parameters body.source.inputFields.
- Update API UpdatePipeline: add request parameters body.source.logstore.project.


2026-07-30 Version: 2.3.1
- Update API CreateExperimentPlan: add request parameters body.pipelineName.
- Update API GetDataset: add response parameters Body.labels.
- Update API GetExperimentPlan: add response parameters Body.pipelineName.
- Update API ListDatasets: add request parameters labels.
- Update API ListDatasets: add response parameters Body.datasets.$.labels.
- Update API UpdateExperimentPlan: add request parameters body.pipelineName.


2026-07-23 Version: 2.3.0
- Support API CreateExperimentPlan.
- Support API CreateExperimentRun.
- Support API DeleteExperimentPlan.
- Support API DeleteExperimentRun.
- Support API GetExperimentPlan.
- Support API GetExperimentRun.
- Support API ListExperimentPlans.
- Support API ListExperimentRuns.
- Support API UpdateExperimentPlan.
- Support API UpdateExperimentRun.


2026-07-21 Version: 2.2.1
- Update API GetDataset: add response parameters Body.isFavorite.
- Update API ListDatasets: add response parameters Body.datasets.$.isFavorite.
- Update API UpdateContextStore: add request parameters body.status.


2026-07-14 Version: 2.2.0
- Support API CreatePipeline.
- Support API PreviewPipeline.
- Update API ExecuteQuery: add request parameters body.version.


2026-07-09 Version: 2.1.0
- Support API CancelPipelineRun.
- Support API CreateEvaluationTask.
- Support API CreateEvaluator.
- Support API CreateEvaluatorSkill.
- Support API DeleteEvaluationRun.
- Support API DeleteEvaluationTask.
- Support API DeleteEvaluator.
- Support API DeleteEvaluatorSkill.
- Support API GetEvaluationRun.
- Support API GetEvaluationTask.
- Support API GetEvaluator.
- Support API GetEvaluatorSkill.
- Support API GetPipelineRun.
- Support API GetPipelineStats.
- Support API ListEvaluationRuns.
- Support API ListEvaluationTasks.
- Support API ListEvaluatorSkills.
- Support API ListEvaluators.
- Support API ListPipelineRuns.
- Support API PausePipeline.
- Support API ResumePipeline.
- Support API RunPipeline.
- Support API TerminatePipeline.
- Support API UpdateEvaluationRun.
- Support API UpdateEvaluationTask.
- Support API UpdateEvaluator.
- Support API UpdateEvaluatorSkill.
- Update API CreateAgentSpace: add request parameters RegionId.
- Update API CreateAgentSpace: add request parameters body.trajectoryStoreEnabled.
- Update API ExecuteQuery: add request parameters body.from.
- Update API ExecuteQuery: add request parameters body.length.
- Update API ExecuteQuery: add request parameters body.maxOutputLength.
- Update API ExecuteQuery: add request parameters body.offset.
- Update API ExecuteQuery: add request parameters body.to.
- Update API ExecuteQuery: add response parameters Body.meta.truncation.
- Update API GetPipeline: add response parameters Body.committedWatermark.
- Update API GetPipeline: add response parameters Body.nextTriggerTime.
- Update API GetPipeline: add response parameters Body.scheduleStatus.
- Update API ListAgentSpaces: add request parameters regionId.
- Update API ListPipelines: add request parameters scheduleStatus.
- Update API ListPipelines: add request parameters scheduleType.
- Update API ListPipelines: add response parameters Body.totalCount.
- Update API ListPipelines: add response parameters Body.pipelines.$.executePolicy.
- Update API ListPipelines: add response parameters Body.pipelines.$.scheduleStatus.
- Update API ListPipelines: add response parameters Body.pipelines.$.scheduleType.


2026-06-22 Version: 2.0.0
- Support API AddDatasetData.
- Delete API AddMem0Memories.
- Delete API DeleteMem0Memories.
- Delete API DeleteMem0Memory.
- Delete API GetMem0Memories.
- Delete API GetMem0Memory.
- Delete API SearchMem0Memories.
- Delete API UpdateMem0Memory.
- Delete API ValidateMem0APIKey.


2026-06-16 Version: 1.0.0
- Generated python 2026-05-20 for AgentLoop.

