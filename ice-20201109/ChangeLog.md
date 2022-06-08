2022-06-08 Version: 1.2.0
- Add page params in ListTemplates API.

2021-12-23 Version: 1.1.6
- Add a new API called SubmitDynamicChartJob, which produce chart video throuth xlsx file.

2021-11-26 Version: 1.1.5
- Add a new API called GetPublicMediaInfo, which gets information of copyrighted public media.
- Add a new API called DescribeMaterialPackageInfo, which describes the available material packages.
- Add a new API called AddFavoritePublicMedia, which adds public media to favorite for the user.
- Add a new API called CancelFavoritePublicMedia, which removes public media from user favorite.
- Add a new API called SearchPublicMediaInfo, which searches copyrighted public media.
- Update the return value of an existed API called ListAllPublicMediaTags, adding field Options.
- Update the return value of an existed API called GetMediaInfo, adding field DynamicMetaData.
- Modify the data type of the return value of an existed API called GetEditingProjectMaterials, where ProjectMaterials should be a list instead of a string.
- Modify the data type of the return value of an existed API called AddEditingProjectMaterials, where ProjectMaterials should be a list instead of a string.
- Update the input params of an existing API called SubmitMediaProducingJob, adding field EditingProduceConfig.

2021-11-16 Version: 1.1.4
- Add a new API called BatchGetMediaInfos, which get multi media infos through mediaids.
- Add a new API called GetTemplateMaterials, which get material urls of VeTemplates.

2021-11-04 Version: 1.1.3
- Add relatedMediaIds param in GetTemplate API.

2021-09-10 Version: 1.1.2
- Add post method to Template API.

2021-08-12 Version: 1.1.1
- Fix GetSmartHandleJob type conversion error.

2021-08-10 Version: 1.1.0
- Add template clipsParam param.

2021-07-15 Version: 1.0.9
- Fix bugs.

2021-07-09 Version: 1.0.8
- Add a new API called ListSysTemplates, which list system templates.
- Add a new API called ListTemplates, which list user templates.
- Add a new API called AddTemplate, which add a new templates.
- Add a new API called UpdateTemplate, which update template configs.
- Add a new API called DeleteTemplate, which delete templates.
- Add vod output config in SubmitH2VJob.
- Add vod output config in SubmitDelogoJob.
- Add vod output config in SubmitMattingJob.

2021-06-03 Version: 1.0.7
- SubmitMediaProducingJob return MediaId in the result.

2021-04-16 Version: 1.0.5
- Add a new API called SubmitH2VJob, which submit horizontal to vertical job.
- Add a new API called SubmitDelogoJob, which submit delogo job.
- Add a new API called SubmitMattingJob, which submit matting job.
- Add a new API called SubmitAudioProduceJob, which produce audio from text.

2021-03-26 Version: 1.0.3
- Add a new API called AddEditingProjectMaterials, which adds one or more materials to the editing project.
- Add a new API called GetEditingProjectMaterials, which gets all the materials in the editing project.
- Add a new API called DeleteEditingProjectMaterials, which deletes specified materials in the editing according to mediaIds or media type .
- Add a new API called ListPublicMediaBasicInfos, which lists the basic information of all public media with a specified media tag.
- Add a new API called ListAllPublicMediaTags, which lists all the media tags for the public media.

2021-02-03 Version: 1.0.0
- Add a new API called RegisterMediaInfo, which registers a new media asset in ICE.
- Add a new API called GetMediaInfo, which returns all the information of a media asset.
- Add a new API called UpdateMediaInfo, which updates the information of a media asset.
- Add a new API called DeleteMediaInfos, which batch deletes media.
- Add a new API called ListMediaBasicInfos, which lists the basic information of all media that match the input criterions.
- Add a new API called CreateEditingProject, which creates an editing project in ICE.
- Add a new API called GetEditingProject, which returns all the information of an editing project.
- Add a new API called UpdateEditingProject, which updates an editing project.
- Add a new API called DeleteEditingProjects, which batch deletes editing projects.
- Add a new API called SearchEditingProjects, which searches editing projects based on the input criterions.
- Add a new API called SubmitMediaProducingJob, which initiates the job for producing media.
- Add a new API called GetMediaProducingJob, which querys the result of the media producing job.

