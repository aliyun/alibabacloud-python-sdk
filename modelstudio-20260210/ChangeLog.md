2026-06-30 Version: 2.0.1
- Update API CreateApiKey: add request parameters auth.modelAccessScope.
- Update API GetApiKey: add response parameters Body.apiKey.auth.modelAccessScope.
- Update API ListApiKeys: add response parameters Body.apiKeys.$.auth.modelAccessScope.
- Update API UpdateApiKey: add request parameters auth.modelAccessScope.


2026-06-29 Version: 2.0.0
- Support API BatchRevokeSeats.
- Support API CreateTokenPlanInviteLink.
- Support API GetOrganization.
- Support API GetOrganizationMemberSeatStats.
- Support API GetSubscriptionStats.
- Support API GetTokenPlanAccountDetail.
- Support API GetTokenPlanInviteLink.
- Support API GetTokenPlanOrgInviteConfig.
- Support API ListOrganizationMembers.
- Support API ListSubscriptionSharedPackages.
- Support API RemoveOrganizationMember.
- Support API RevokeTokenPlanInviteLink.
- Support API RotateTokenPlanKey.
- Support API SetTokenPlanOrgInviteConfig.
- Support API UpdateOrganization.
- Support API UpdateOrganizationMember.
- Update API AddOrganizationMember: delete request parameters CallerUacAccountId.
- Update API AddOrganizationMember: delete request parameters NamespaceId.
- Update API AddOrganizationMember: delete request parameters OrgId.
- Update API BatchAssignSeats: delete request parameters AccountIdsStr.
- Update API BatchAssignSeats: delete request parameters CallerUacAccountId.
- Update API BatchAssignSeats: delete request parameters NamespaceId.
- Update API BatchAssignSeats: delete request parameters WorkspaceId.
- Update API CreateTokenPlanKey: delete request parameters CallerUacAccountId.
- Update API CreateTokenPlanKey: delete request parameters NamespaceId.
- Update API CreateTokenPlanKey: delete request parameters WorkspaceId.
- Update API GetSubscriptionSeatDetails: delete request parameters CallerUacAccountId.
- Update API GetSubscriptionSeatDetails: delete request parameters NamespaceId.
- Update API GetSubscriptionSeatDetails: delete request parameters StatusListStr.
- Update API ListApiKeys: add request parameters order.
- Update API ListApiKeys: add request parameters orderBy.


2026-06-18 Version: 1.3.0
- Support API AddOrganizationMember.
- Support API BatchAssignSeats.
- Support API CreateTokenPlanKey.
- Support API GetSubscriptionSeatDetails.


2026-06-05 Version: 1.2.0
- Support API DeleteWorkspace.


2026-05-22 Version: 1.1.0
- Support API DisableApiKey.
- Support API EnableApiKey.
- Support API ResetApiKey.
- Update API CreateApiKey: add request parameters auth.
- Update API GetApiKey: add response parameters Body.apiKey.auth.
- Update API ListApiKeys: add response parameters Body.apiKeys.$.auth.
- Update API UpdateApiKey: add request parameters auth.


2026-04-27 Version: 1.0.1
- Update API CreateWorkspace: add request parameters serviceSite.
- Update API ListWorkspaces: add request parameters workspaceId.


2026-03-31 Version: 1.0.0
- Generated python 2026-02-10 for ModelStudio.

