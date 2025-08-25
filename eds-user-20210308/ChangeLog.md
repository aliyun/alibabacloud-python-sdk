2025-08-25 Version: 1.6.3
- Update API DescribeMfaDevices: add request parameters Filter.
- Update API DescribeMfaDevices: add response parameters Body.MfaDevices.$.AdUser.


2025-08-12 Version: 1.6.2
- Update API DescribeOrgs: add request parameters ShowExtras.
- Update API DescribeOrgs: add response parameters Body.Orgs.$.OrgNamePath.


2025-07-30 Version: 1.6.1
- Update API CreateGroup: add request parameters Description.
- Update API DescribeGroupUser: add request parameters Filter.
- Update API DescribeGroupUser: add request parameters MaxResults.
- Update API DescribeGroupUser: add request parameters NextToken.
- Update API DescribeGroupUser: add response parameters Body.NextToken.
- Update API DescribeGroupUser: add response parameters Body.Users.$.Remark.
- Update API DescribeGroups: add request parameters PageNumber.
- Update API DescribeGroups: add request parameters PageSize.
- Update API DescribeGroups: add request parameters TransferFileNeedApproval.
- Update API DescribeGroups: add response parameters Body.Count.
- Update API DescribeGroups: add response parameters Body.Groups.$.AuthedResources.
- Update API DescribeGroups: add response parameters Body.Groups.$.CreateTime.
- Update API DescribeGroups: add response parameters Body.Groups.$.Description.
- Update API DescribeGroups: add response parameters Body.Groups.$.TransferFileNeedApproval.
- Update API DescribeGroups: add response parameters Body.Groups.$.UserCount.
- Update API DescribeUsers: add request parameters ExcludeGroupId.
- Update API DescribeUsers: add response parameters Body.Users.$.EnableAdminAccess.
- Update API ModifyGroup: add request parameters Description.
- Update API RemoveGroup: add request parameters GroupIds.


2025-07-02 Version: 1.6.0
- Support API CreateGroup.
- Support API DescribeGroupUser.
- Support API DescribeGroups.
- Support API ModifyGroup.
- Support API MoveUserOrg.
- Support API RemoveGroup.
- Support API UserBatchJoinGroup.
- Support API UserBatchQuitGroup.


2025-06-07 Version: 1.5.2
- Update API DescribeUsers: add request parameters Status.
- Update API DescribeUsers: add response parameters Body.Users.$.Orgs.$.OrgNamePath.
- Update API FilterUsers: add response parameters Body.Users.$.OrgList.$.OrgNamePath.


2025-05-22 Version: 1.5.1
- Update API DescribeResourceGroups: add response parameters Body.ResourceGroup.$.AppRules.
- Update API DescribeResourceGroups: add response parameters Body.ResourceGroup.$.Timers.$.BindStatus.
- Update API DescribeResourceGroups: add response parameters Body.ResourceGroup.$.Timers.$.TimerStatus.


2025-04-27 Version: 1.5.0
- Support API CreateResourceGroup.
- Support API DeleteResourceGroup.
- Support API DescribeResourceGroups.


2025-04-25 Version: 1.4.1
- Update API CreateUsers: add response parameters Body.AllSucceed.


2025-04-23 Version: 1.4.0
- Support API CreateOrg.
- Support API DescribeOrgByLayer.
- Support API InitTenantAlias.
- Support API ModifyOrg.
- Support API MoveOrg.
- Support API RemoveOrg.


2025-03-25 Version: 1.3.3
- Update API DescribeUsers: add param FilterWithAssignedResource.
- Update API DescribeUsers: add param IsQueryAllSubOrgs.
- Update API DescribeUsers: update response param.
- Update API FilterUsers: add param IncludeOrgInfo.
- Update API FilterUsers: add param IncludeSupportIdps.
- Update API FilterUsers: update response param.


2024-12-11 Version: 1.3.2
- Update API CreateUsers: update param Users.
- Update API FilterUsers: add param IsQueryAllSubOrgs.


2024-11-07 Version: 1.3.1
- Generated python 2021-03-08 for eds-user.

2024-11-06 Version: 1.3.0
- Support API ChangeUserPassword.
- Update API LockUsers: add param LogoutSession.


2024-09-24 Version: 1.2.0
- Support API BatchSetDesktopManager.
- Support API DescribeOrgs.
- Update API CreateUsers: add param IsLocalAdmin.
- Update API CreateUsers: add param PasswordExpireDays.
- Update API DescribeUsers: add param FilterWithAssignedResources.
- Update API DescribeUsers: add param ShowExtras.
- Update API DescribeUsers: update param BizType.
- Update API DescribeUsers: update param SolutionId.
- Update API DescribeUsers: update response param.
- Update API FilterUsers: add param Status.
- Update API FilterUsers: update response param.


2024-01-16 Version: 1.1.1
- Generated python 2021-03-08 for eds-user.

2023-09-25 Version: 1.1.0
- Generated python 2021-03-08 for eds-user.

2023-08-31 Version: 1.0.2
- Generated python 2021-03-08 for eds-user.

2023-08-22 Version: 1.0.1
- Generated python 2021-03-08 for eds-user.

2023-05-17 Version: 1.0.0
- Org.

