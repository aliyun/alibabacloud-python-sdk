2025-07-02 Version: 1.4.0
- Support API ListBoundDevices.
- Support API ListUnbindDevices.
- Update API AddTerminal: add request parameters ClientType.
- Update API AddTerminal: add request parameters MainBizType.
- Update API AddTerminal: add request parameters Uuid.
- Update API AddTerminals: add request parameters MainBizType.
- Update API BindPasswordFreeLoginUser: add request parameters MainBizType.
- Update API CheckUuidValid: add request parameters ClientVersion.
- Update API CheckUuidValid: add request parameters LoginRegionId.
- Update API CheckUuidValid: add request parameters LoginToken.
- Update API CheckUuidValid: add request parameters SessionId.
- Update API CreateAppOtaTask: add request parameters TenantIdList.
- Update API CreateAppOtaVersion: add request parameters RelationVersionUids.
- Update API DescribeAppOtaVersion: add request parameters NullChannel.
- Update API DescribeAppOtaVersion: add request parameters OtaType.
- Update API GetDeviceOtaInfo: add response parameters Body.Data.Version.WyForceUpgrade.
- Update API ListDevices: add request parameters LastLoginUser.
- Update API ListTerminals: add request parameters MainBizType.
- Update API RegisterDevice: add response parameters Body.Data.NewUpgrade.
- Update API ReportUserFbIssue: add request parameters ClientAppVersion.
- Update API SendOpsMessageToTerminals: add response parameters Body.Data.
- Update API UnbindPasswordFreeLoginUser: add request parameters MainBizType.
- Update API UpdateTerminalPolicy: add request parameters AllowManualLockScreen.
- Update API UpdateTerminalPolicy: add request parameters CustomScreenCastRes.
- Update API UpdateTerminalPolicy: add request parameters EnableControlPanel.
- Update API UpdateTerminalPolicy: add request parameters EnableImmersiveMode.
- Update API UpdateTerminalPolicy: add request parameters EnableLockScreenHotKey.
- Update API UpdateTerminalPolicy: add request parameters EnableScanLogin.
- Update API UpdateTerminalPolicy: add request parameters EnableSmsLogin.
- Update API UpdateTerminalPolicy: add request parameters FollowCloudReboot.
- Update API UpdateTerminalPolicy: add request parameters FollowCloudShutdown.
- Update API UpdateTerminalPolicy: add request parameters FollowTerminalReboot.
- Update API UpdateTerminalPolicy: add request parameters FollowTerminalShutdown.
- Update API UpdateTerminalPolicy: add request parameters ForceSetPinCode.
- Update API UpdateTerminalPolicy: add request parameters LockScreenPasswordRequired.
- Update API UpdateTerminalPolicy: add request parameters LockScreenTimeout.
- Update API UpdateTerminalPolicy: add request parameters MainBizType.
- Update API UpdateTerminalPolicy: add request parameters RunningMode.
- Update API UpdateTerminalPolicy: add request parameters ScreenCastResPaths.
- Update API UpdateTerminalPolicy: add request parameters UnlockMethod.


2024-10-08 Version: 1.3.0
- Support API AddTerminals.


2024-10-08 Version: 1.2.1
- Update API CheckUuidValid: add param WosAppVersion.
- Update API CheckUuidValid: update response param.
- Update API ListTerminals: add param InManage.
- Update API ListTerminals: add param PasswordFreeLoginUser.
- Update API ListTerminals: add param WithBindUser.
- Update API ListTerminals: update param SerialNumbers.
- Update API ListTerminals: update param Uuids.
- Update API ListTerminals: update response param.


2024-09-11 Version: 1.2.0
- Support API UnbindPasswordFreeLoginUser.


2024-09-11 Version: 1.1.0
- Support API BindPasswordFreeLoginUser.


2024-08-30 Version: 1.0.4
- Update API DescribeAppOtaVersion: update response param.
- Update API UpdateTerminalPolicy: add param BackgroundModeTitle.
- Update API UpdateTerminalPolicy: add param EnableBackgroundMode.
- Update API UpdateTerminalPolicy: add param EnableScheduledReboot.
- Update API UpdateTerminalPolicy: add param ScheduledReboot.


2024-08-27 Version: 1.0.3
- Update API ListTerminals: update response param.


2024-08-13 Version: 1.0.2
- Update API ListTerminals: add param SerialNumbers.
- Update API ListTerminals: add param Uuids.


2024-08-13 Version: 1.0.1
- Update API SendOpsMessageToTerminals: add param Delay.


2024-08-12 Version: 1.0.0
- Generated python 2021-04-20 for wyota.

