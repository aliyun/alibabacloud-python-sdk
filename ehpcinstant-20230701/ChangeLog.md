2025-07-04 Version: 2.0.5
- Update API DeleteJobs: add request parameters JobScheduler.


2025-07-03 Version: 2.0.4
- Update API GetImage: add request parameters AdditionalRegionIds.
- Update API GetImage: add response parameters Body.Image.AdditionalRegionsInfo.


2025-06-12 Version: 2.0.3
- Update API CreateJob: add request parameters DeploymentPolicy.Pool.
- Update API CreateJob: add request parameters DeploymentPolicy.Priority.
- Update API CreateJob: add request parameters Tasks.$.TaskSpec.Resource.InstanceTypes.
- Update API CreateJob: add request parameters Tasks.$.TaskSpec.TaskExecutor.$.Container.Arg.
- Update API CreateJob: add request parameters Tasks.$.TaskSpec.TaskExecutor.$.VM.Password.
- Update API CreateJob: add request parameters Tasks.$.TaskSpec.VolumeMount.$.ReadOnly.
- Update API GetJob: add response parameters Body.JobInfo.Tasks.$.TaskSpec.Resource.InstanceTypes.
- Update API GetJob: add response parameters Body.JobInfo.Tasks.$.TaskSpec.TaskExecutor.$.VM.UserName.


2025-05-09 Version: 2.0.2
- Update API GetJob: add response parameters Body.JobInfo.AppExtraInfo.
- Update API ListJobs: add response parameters Body.JobList.$.AppExtraInfo.


2025-03-31 Version: 2.0.1
- Update API CreateJob: add request parameters DeploymentPolicy.Level.
- Update API GetJob: add response parameters Body.JobInfo.DeploymentPolicy.Level.
- Update API GetJob: add response parameters Body.JobInfo.DeploymentPolicy.Network.EnableENIMapping.


2025-02-12 Version: 2.0.0
- Update API CreateJob: add param SecurityPolicy.
- Update API ListExecutors: update param PageNumber.
- Update API ListExecutors: update param PageSize.
- Update API ListExecutors: update response param.
- Update API ListJobExecutors: update param PageNumber.
- Update API ListJobExecutors: update param PageSize.
- Update API ListJobExecutors: update response param.
- Update API ListJobs: update param PageNumber.
- Update API ListJobs: update param PageSize.
- Update API ListJobs: update response param.


2024-12-20 Version: 1.2.0
- Support API CreatePool.
- Support API DeletePool.
- Support API GetAppVersions.
- Support API GetPool.
- Support API ListPools.
- Support API UpdatePool.
- Update API CreateJob: update param Tasks.
- Update API GetImage: update response param.
- Update API ListImages: add param Mode.
- Update API ListImages: update response param.


2024-11-18 Version: 1.1.1
- Update API ListImages: update response param.


2024-11-13 Version: 1.1.0
- Support API ListTagResources.
- Support API TagResources.
- Support API UnTagResources.
- Update API AddImage: add param ImageType.
- Update API CreateJob: update param DeploymentPolicy.
- Update API GetJob: update response param.
- Update API ListExecutors: update param Filter.
- Update API ListExecutors: update response param.
- Update API ListJobExecutors: update response param.
- Update API ListJobs: update response param.
- Update API RemoveImage: add param ImageType.


2024-08-14 Version: 1.0.4
- Update API ListExecutors: update response param.
- Update API ListJobExecutors: update response param.


2024-07-31 Version: 1.0.3
- Update API CreateJob: add param JobScheduler.
- Update API CreateJob: update param Tasks.
- Update API CreateJob: update response param.
- Update API GetImage: add param ImageCategory.
- Update API GetImage: add param ImageType.
- Update API GetImage: update response param.
- Update API GetJob: update response param.
- Update API ListImages: add param ImageCategory.
- Update API ListImages: add param ImageType.
- Update API ListImages: update response param.


2024-05-15 Version: 1.0.2
- Update API CreateJob: update param Tasks.
- Update API CreateJob: update response param.
- Update API GetImage: add param ImageCategory.
- Update API GetImage: add param ImageType.
- Update API GetImage: update response param.
- Update API ListImages: add param ImageCategory.
- Update API ListImages: add param ImageType.
- Update API ListImages: update response param.


2024-05-11 Version: 1.0.1
- Update API CreateJob: update response param.


2024-04-24 Version: 1.0.0
- Generated python 2023-07-01 for EhpcInstant.

