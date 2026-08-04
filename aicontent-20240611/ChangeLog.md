2026-08-04 Version: 7.6.0
- Support API ModelRouterBatchCreateMemberApiKeys.
- Support API ModelRouterBatchCreateModel.
- Support API ModelRouterBatchDisableMemberApiKeys.
- Support API ModelRouterBatchResetMemberAuthorization.
- Support API ModelRouterBatchSetMemberAuthorization.
- Support API ModelRouterConfigureMemberBalance.
- Support API ModelRouterCreateMemberApiKey.
- Support API ModelRouterCreateMemberBalanceTransaction.
- Support API ModelRouterCreateMemberSubscription.
- Support API ModelRouterCreateUser.
- Support API ModelRouterDeleteUser.
- Support API ModelRouterExportMemberBalanceOrders.
- Support API ModelRouterGetDeptBalanceSummary.
- Support API ModelRouterGetMemberApiKeys.
- Support API ModelRouterGetMemberBalance.
- Support API ModelRouterGetMemberBalanceLogs.
- Support API ModelRouterGetUserRoles.
- Support API ModelRouterListDeptMembers.
- Support API ModelRouterListMemberBalanceOrders.
- Support API ModelRouterListMemberSubscriptions.
- Support API ModelRouterQueryModelGroupUsers.
- Support API ModelRouterQueryUserList.
- Support API ModelRouterResetMemberAuthorization.
- Support API ModelRouterSearchClientTree.
- Support API ModelRouterSetMemberAuthorization.
- Support API ModelRouterSetUserRoles.
- Support API ModelRouterStopMemberSubscription.
- Support API ModelRouterTransferToMember.
- Support API ModelRouterUpdateUser.
- Update API ModelRouterQueryApiKeyList: add request parameters includeMemberKeys.
- Update API ModelRouterQueryApiKeyList: add request parameters memberUserIds.
- Update API ModelRouterQueryBillingCostBreakdown: add request parameters memberUserIds.
- Update API ModelRouterQueryClientList: add request parameters parentId.
- Update API ModelRouterQueryCostModelDetail: add request parameters memberUserIds.
- Update API ModelRouterQueryCostModelList: add request parameters memberUserIds.
- Update API ModelRouterQueryCostOverviewMetrics: add request parameters memberUserIds.
- Update API ModelRouterQueryCostTrendMetrics: add request parameters memberUserIds.
- Update API ModelRouterQueryModelGroupsByApiKey: add response parameters Body.data.bindType.
- Update API ModelRouterQueryObservationCharts: add request parameters memberUserIds.
- Update API ModelRouterQueryObservationLogs: add request parameters memberUserIds.
- Update API ModelRouterQueryObservationMetrics: add request parameters memberUserIds.
- Update API ModelRouterQueryUsageBreakdown: add request parameters memberUserIds.


2026-07-31 Version: 7.5.0
- Support API ModelRouterBatchBindModelGroup.
- Support API ModelRouterCreateModelGroup.
- Support API ModelRouterDeleteModelGroup.
- Support API ModelRouterListBalanceOrders.
- Support API ModelRouterQueryModelGroup.
- Support API ModelRouterQueryModelGroupClients.
- Support API ModelRouterQueryModelGroupList.
- Support API ModelRouterQueryModelGroupModels.
- Support API ModelRouterQueryModelGroupsByApiKey.
- Support API ModelRouterUpdateModelGroup.


2026-07-31 Version: 7.5.0
- Support API ModelRouterBatchBindModelGroup.
- Support API ModelRouterCreateModelGroup.
- Support API ModelRouterDeleteModelGroup.
- Support API ModelRouterListBalanceOrders.
- Support API ModelRouterQueryModelGroup.
- Support API ModelRouterQueryModelGroupClients.
- Support API ModelRouterQueryModelGroupList.
- Support API ModelRouterQueryModelGroupModels.
- Support API ModelRouterQueryModelGroupsByApiKey.
- Support API ModelRouterUpdateModelGroup.


2026-07-21 Version: 7.4.0
- Support API ModelRouterCreateSubscription.
- Support API ModelRouterListSubscriptions.
- Support API ModelRouterStopSubscription.
- Update API ModelRouterCreateBalanceTransaction: add request parameters body.balanceType.
- Update API ModelRouterCreateBalanceTransaction: add request parameters body.idempotencyKey.


2026-05-20 Version: 7.3.3
- Update API ModelRouterQueryBillingCostBreakdown: add request parameters apiKeyId.
- Update API ModelRouterQueryCostModelDetail: add request parameters apiKeyId.
- Update API ModelRouterQueryCostModelList: add request parameters apiKeyId.
- Update API ModelRouterQueryCostOverviewMetrics: add request parameters apiKeyId.
- Update API ModelRouterQueryCostTrendMetrics: add request parameters apiKeyId.
- Update API ModelRouterQueryUsageBreakdown: add request parameters apiKeyId.
- Update API ModelRouterQueryUsageBreakdown: add request parameters clientId.


2026-05-13 Version: 7.3.2
- Update API ModelRouterQueryBillingCostBreakdown: add request parameters clientId.
- Update API ModelRouterQueryBillingCostBreakdown: add request parameters modelId.
- Update API ModelRouterQueryBillingCostBreakdown: add request parameters modelTypes.


2026-04-30 Version: 7.3.1
- Generated python 20240611 for AiContent.

2026-04-30 Version: 7.3.0
- Support API ModelRouterConfigureClientBalance.
- Support API ModelRouterCreateBalanceTransaction.
- Support API ModelRouterGetClientBalance.
- Support API ModelRouterGetClientBalanceLogs.


2026-04-27 Version: 7.2.0
- Support API ModelRouterQueryBillingCostBreakdown.
- Support API ModelRouterQueryUsageBreakdown.


2026-04-23 Version: 7.1.0
- Support API ModelRouterBillingCostTabs.
- Support API ModelRouterCreateBillingRule.
- Support API ModelRouterQueryBillingRuleList.
- Support API ModelRouterQueryClientDiscountLogs.
- Support API ModelRouterQueryClientTree.
- Support API ModelRouterQueryCostModelDetail.
- Support API ModelRouterQueryCostModelList.
- Support API ModelRouterQueryCostOverviewMetrics.
- Support API ModelRouterQueryCostTrendMetrics.
- Support API ModelRouterUpdateBillingRule.


2026-04-16 Version: 7.0.2
- Update API ModelRouterCreateClient: add request parameters body.discount.
- Update API ModelRouterQueryModelList: add response parameters Body.maxResults.
- Update API ModelRouterUpdateClient: add request parameters body.discount.


2026-03-23 Version: 7.0.0
- Update API ModelRouterQueryApiKeyList: update response parameters Body.data' type has changed.
- Update API ModelRouterQueryApiKeyList: delete response parameters Body.data.$.
- Update API ModelRouterQueryApiKeyList: delete response parameters Body.nextToken.
- Update API ModelRouterQueryApiKeyList: delete response parameters Body.pageIndex.
- Update API ModelRouterQueryApiKeyList: delete response parameters Body.pageSize.
- Update API ModelRouterQueryApiKeyList: delete response parameters Body.skip.
- Update API ModelRouterQueryApiKeyList: delete response parameters Body.totalCount.
- Update API ModelRouterQueryClientList: update response parameters Body.data' type has changed.
- Update API ModelRouterQueryClientList: delete response parameters Body.data.$.
- Update API ModelRouterQueryClientList: delete response parameters Body.maxResults.
- Update API ModelRouterQueryClientList: delete response parameters Body.nextToken.
- Update API ModelRouterQueryClientList: delete response parameters Body.pageIndex.
- Update API ModelRouterQueryClientList: delete response parameters Body.pageSize.
- Update API ModelRouterQueryClientList: delete response parameters Body.skip.
- Update API ModelRouterQueryClientList: delete response parameters Body.totalCount.
- Update API ModelRouterQueryConversationList: update response parameters Body.data' type has changed.
- Update API ModelRouterQueryConversationList: delete response parameters Body.data.$.
- Update API ModelRouterQueryConversationList: delete response parameters Body.maxResults.
- Update API ModelRouterQueryConversationList: delete response parameters Body.nextToken.
- Update API ModelRouterQueryConversationList: delete response parameters Body.pageIndex.
- Update API ModelRouterQueryConversationList: delete response parameters Body.pageSize.
- Update API ModelRouterQueryConversationList: delete response parameters Body.skip.
- Update API ModelRouterQueryConversationList: delete response parameters Body.totalCount.
- Update API ModelRouterQueryModelList: update response parameters Body.data' type has changed.
- Update API ModelRouterQueryModelList: delete response parameters Body.data.$.
- Update API ModelRouterQueryModelList: delete response parameters Body.maxResults.
- Update API ModelRouterQueryModelList: delete response parameters Body.nextToken.
- Update API ModelRouterQueryModelList: delete response parameters Body.pageIndex.
- Update API ModelRouterQueryModelList: delete response parameters Body.pageSize.
- Update API ModelRouterQueryModelList: delete response parameters Body.skip.
- Update API ModelRouterQueryModelList: delete response parameters Body.totalCount.
- Update API ModelRouterQueryNacosProviders: update response parameters Body.data.$' type has changed.
- Update API ModelRouterQueryNacosProviders: delete response parameters Body.maxResults.
- Update API ModelRouterQueryNacosProviders: delete response parameters Body.nextToken.
- Update API ModelRouterQueryNacosProviders: delete response parameters Body.pageIndex.
- Update API ModelRouterQueryNacosProviders: delete response parameters Body.pageSize.
- Update API ModelRouterQueryNacosProviders: delete response parameters Body.skip.
- Update API ModelRouterQueryNacosProviders: delete response parameters Body.totalCount.
- Update API ModelRouterQueryNacosTags: update response parameters Body.data.$' type has changed.
- Update API ModelRouterQueryNacosTags: delete response parameters Body.maxResults.
- Update API ModelRouterQueryNacosTags: delete response parameters Body.nextToken.
- Update API ModelRouterQueryNacosTags: delete response parameters Body.pageIndex.
- Update API ModelRouterQueryNacosTags: delete response parameters Body.pageSize.
- Update API ModelRouterQueryNacosTags: delete response parameters Body.skip.
- Update API ModelRouterQueryNacosTags: delete response parameters Body.totalCount.
- Update API ModelRouterQueryObservationLogs: update response parameters Body.data' type has changed.
- Update API ModelRouterQueryObservationLogs: delete response parameters Body.data.$.
- Update API ModelRouterQueryObservationLogs: delete response parameters Body.pageIndex.
- Update API ModelRouterQueryObservationLogs: delete response parameters Body.pageSize.
- Update API ModelRouterQueryObservationLogs: delete response parameters Body.skip.
- Update API ModelRouterQueryObservationLogs: delete response parameters Body.totalCount.
- Update API ModelRouterQueryObservationMetrics: update response parameters Body.data' type has changed.
- Update API ModelRouterQueryObservationMetrics: update response parameters Body.data' ref has changed.
- Update API ModelRouterQueryObservationMetrics: delete response parameters Body.data.$.
- Update API ModelRouterQueryObservationMetrics: delete response parameters Body.maxResults.
- Update API ModelRouterQueryObservationMetrics: delete response parameters Body.nextToken.
- Update API ModelRouterQueryObservationMetrics: delete response parameters Body.pageIndex.
- Update API ModelRouterQueryObservationMetrics: delete response parameters Body.pageSize.
- Update API ModelRouterQueryObservationMetrics: delete response parameters Body.skip.
- Update API ModelRouterQueryObservationMetrics: delete response parameters Body.totalCount.


2026-03-19 Version: 6.0.0
- Delete API ModelRouterQueryModelWithApiKey.
- Update API ModelRouterCreateModel: add request parameters body.maxInputLength.
- Update API ModelRouterCreateModel: add request parameters body.maxOutputLength.


2026-03-18 Version: 5.0.0
- Support API AliyunConsoleOpenApiQueryPaidResource.
- Support API ModelRouterChatCompletions.
- Support API ModelRouterCopyApiKey.
- Support API ModelRouterCreateApiKey.
- Support API ModelRouterCreateClient.
- Support API ModelRouterCreateConversation.
- Support API ModelRouterCreateModel.
- Support API ModelRouterDeleteApiKey.
- Support API ModelRouterDeleteClient.
- Support API ModelRouterDeleteConversation.
- Support API ModelRouterDeleteModel.
- Support API ModelRouterQueryApiKey.
- Support API ModelRouterQueryApiKeyList.
- Support API ModelRouterQueryClientList.
- Support API ModelRouterQueryConversation.
- Support API ModelRouterQueryConversationList.
- Support API ModelRouterQueryModel.
- Support API ModelRouterQueryModelList.
- Support API ModelRouterQueryModelWithApiKey.
- Support API ModelRouterQueryNacosProviders.
- Support API ModelRouterQueryNacosTags.
- Support API ModelRouterQueryObservationCharts.
- Support API ModelRouterQueryObservationLogs.
- Support API ModelRouterQueryObservationMetrics.
- Support API ModelRouterUpdateClient.
- Support API ModelRouterUpdateConversation.
- Support API ModelRouterUpdateModel.
- Delete API ExecuteHundredThousandWhysDialogue.


2025-05-21 Version: 4.0.0
- Update API ListTextbookAssistantArticleDetails: add response parameters Body.data.$.sceneList.$.sceneTranslate.
- Update API ListTextbookAssistantArticleDetails: delete response parameters Body.data.$.sceneList.$.sceneTransLate.
- Update API ListTextbookAssistantBookDirectories: add response parameters Body.data.directoryTree.$.unit.
- Update API ListTextbookAssistantSceneDetails: add response parameters Body.data.$.sceneTranslate.


2025-05-16 Version: 3.0.0
- Support API CountOralEvaluationStatisticsCalls.
- Support API CountOralEvaluationStatisticsConcurrent.
- Support API CountOralEvaluationStatisticsError.
- Support API ExecuteHundredThousandWhysDialogue.
- Update API ExecuteAITeacherChineseCompositionTutoringWorkflowRun: delete request parameters callerParentId.
- Update API ExecuteAITeacherChineseCompositionTutoringWorkflowRun: delete request parameters callerType.
- Update API ExecuteAITeacherChineseCompositionTutoringWorkflowRun: delete request parameters callerUid.
- Update API ExecuteAITeacherChineseCompositionTutoringWorkflowRun: delete request parameters stsTokenCallerUid.
- Update API ListTextbookAssistantGradeVolumes: update response parameters Body.data' type has changed.
- Update API ListTextbookAssistantGradeVolumes: delete response parameters Body.data.


2025-03-27 Version: 2.1.0
- Support API ExecuteTextbookAssistantSseDialogue.
- Support API ListTextbookAssistantArticleDetails.
- Support API ListTextbookAssistantSceneDetails.


2025-03-26 Version: 2.0.0
- Support API CreateAccessWarrant.
- Support API CreateProject.
- Support API ExecuteAITeacherChineseCompositionTutoringWorkflowRun.
- Support API ExecuteAITeacherEnglishCompositionTutoringWorkflowRun.
- Support API ExecuteAITeacherEnglishParaphraseChatMessage.
- Support API QueryApplicationAccessId.
- Support API QueryProject.
- Support API QueryProjectList.
- Support API QueryPurchasedService.
- Support API UpdateProject.
- Update API AliyunConsoleOpenApiQueryAliyunConsoleServiceList: update response parameters Body.data.$' type has changed.
- Update API AliyunConsoleOpenApiQueryAliyunConsoleServiceList: update response parameters Body.data.$' ref has changed.
- Update API AliyunConsoleOpenApiQueryAliyunConsoleServiceList: delete response parameters Body.data.$.


2025-01-16 Version: 1.4.0
- Support API ExecuteTextbookAssistantDialogue.
- Support API ExecuteTextbookAssistantDifficulty.
- Support API ExecuteTextbookAssistantGrammarCheck.
- Support API ExecuteTextbookAssistantRefineByContext.
- Support API ExecuteTextbookAssistantRetryConversation.
- Support API ExecuteTextbookAssistantStartConversation.
- Support API ExecuteTextbookAssistantSuggestion.
- Support API ExecuteTextbookAssistantTranslate.
- Support API GetTextbookAssistantToken.
- Support API ListTextbookAssistantArticles.
- Support API ListTextbookAssistantBookDirectories.
- Support API ListTextbookAssistantBooks.
- Support API ListTextbookAssistantGradeVolumes.


2025-01-02 Version: 1.3.1
- Update API GetAITeacherSyncDialogueSuggestion: update response param.


2024-12-27 Version: 1.3.0
- Support API ExecuteAITeacherExpansionDialogue.
- Support API ExecuteAITeacherExpansionDialogueRefine.
- Support API ExecuteAITeacherExpansionDialogueTranslate.
- Support API ExecuteAITeacherGrammarCheck.
- Support API ExecuteAITeacherSyncDialogue.
- Support API ExecuteAITeacherSyncDialogueTranslate.
- Support API GetAITeacherExpansionDialogueSuggestion.
- Support API GetAITeacherSyncDialogueSuggestion.


2024-12-20 Version: 1.2.0
- Support API AITeacherExpansionPracticeTaskGenerate.
- Support API AITeacherSyncPracticeTaskGenerate.


2024-10-12 Version: 1.1.0
- Support API AliyunConsoleOpenApiQueryAliyunConsoleServiceList.
- Support API PersonalizedTextToImageAddInferenceJob.
- Support API PersonalizedTextToImageQueryImageAsset.
- Support API PersonalizedTextToImageQueryPreModelInferenceJobInfo.


2024-10-12 Version: 1.1.0
- Support API AliyunConsoleOpenApiQueryAliyunConsoleServiceList.
- Support API PersonalizedTextToImageAddInferenceJob.
- Support API PersonalizedTextToImageQueryImageAsset.
- Support API PersonalizedTextToImageQueryPreModelInferenceJobInfo.


2024-08-01 Version: 1.0.0
- Generated python 20240611 for AiContent.

