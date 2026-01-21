# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_yundun_bastionhost20191209 import models as main_models
from darabonba.model import DaraModel

class GetPolicyResponseBody(DaraModel):
    def __init__(
        self,
        policy: main_models.GetPolicyResponseBodyPolicy = None,
        request_id: str = None,
    ):
        # The details of the control policy.
        self.policy = policy
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.policy:
            self.policy.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.policy is not None:
            result['Policy'] = self.policy.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Policy') is not None:
            temp_model = main_models.GetPolicyResponseBodyPolicy()
            self.policy = temp_model.from_map(m.get('Policy'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetPolicyResponseBodyPolicy(DaraModel):
    def __init__(
        self,
        access_time_range_config: main_models.GetPolicyResponseBodyPolicyAccessTimeRangeConfig = None,
        approval_config: main_models.GetPolicyResponseBodyPolicyApprovalConfig = None,
        command_config: main_models.GetPolicyResponseBodyPolicyCommandConfig = None,
        comment: str = None,
        ipacl_config: main_models.GetPolicyResponseBodyPolicyIPAclConfig = None,
        policy_id: str = None,
        policy_name: str = None,
        priority: int = None,
        protocol_config: main_models.GetPolicyResponseBodyPolicyProtocolConfig = None,
    ):
        # The details of the logon period restrictions.
        self.access_time_range_config = access_time_range_config
        # The O\\&M approval setting.
        self.approval_config = approval_config
        # The details of the command policy.
        self.command_config = command_config
        # The description of the control policy.
        self.comment = comment
        # The access control settings on source IP addresses.
        self.ipacl_config = ipacl_config
        # The ID of the control policy.
        self.policy_id = policy_id
        # The name of the control policy.
        self.policy_name = policy_name
        # The priority of the control policy. A smaller value indicates a higher priority.
        self.priority = priority
        # The details of protocol control.
        self.protocol_config = protocol_config

    def validate(self):
        if self.access_time_range_config:
            self.access_time_range_config.validate()
        if self.approval_config:
            self.approval_config.validate()
        if self.command_config:
            self.command_config.validate()
        if self.ipacl_config:
            self.ipacl_config.validate()
        if self.protocol_config:
            self.protocol_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_time_range_config is not None:
            result['AccessTimeRangeConfig'] = self.access_time_range_config.to_map()

        if self.approval_config is not None:
            result['ApprovalConfig'] = self.approval_config.to_map()

        if self.command_config is not None:
            result['CommandConfig'] = self.command_config.to_map()

        if self.comment is not None:
            result['Comment'] = self.comment

        if self.ipacl_config is not None:
            result['IPAclConfig'] = self.ipacl_config.to_map()

        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id

        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.protocol_config is not None:
            result['ProtocolConfig'] = self.protocol_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessTimeRangeConfig') is not None:
            temp_model = main_models.GetPolicyResponseBodyPolicyAccessTimeRangeConfig()
            self.access_time_range_config = temp_model.from_map(m.get('AccessTimeRangeConfig'))

        if m.get('ApprovalConfig') is not None:
            temp_model = main_models.GetPolicyResponseBodyPolicyApprovalConfig()
            self.approval_config = temp_model.from_map(m.get('ApprovalConfig'))

        if m.get('CommandConfig') is not None:
            temp_model = main_models.GetPolicyResponseBodyPolicyCommandConfig()
            self.command_config = temp_model.from_map(m.get('CommandConfig'))

        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('IPAclConfig') is not None:
            temp_model = main_models.GetPolicyResponseBodyPolicyIPAclConfig()
            self.ipacl_config = temp_model.from_map(m.get('IPAclConfig'))

        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')

        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('ProtocolConfig') is not None:
            temp_model = main_models.GetPolicyResponseBodyPolicyProtocolConfig()
            self.protocol_config = temp_model.from_map(m.get('ProtocolConfig'))

        return self

class GetPolicyResponseBodyPolicyProtocolConfig(DaraModel):
    def __init__(
        self,
        rdp: main_models.GetPolicyResponseBodyPolicyProtocolConfigRDP = None,
        ssh: main_models.GetPolicyResponseBodyPolicyProtocolConfigSSH = None,
    ):
        # The configuration details of Remote Desktop Protocol (RDP) options.
        self.rdp = rdp
        # The configuration details of SSH and SSH File Transfer Protocol (SFTP) options.
        self.ssh = ssh

    def validate(self):
        if self.rdp:
            self.rdp.validate()
        if self.ssh:
            self.ssh.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.rdp is not None:
            result['RDP'] = self.rdp.to_map()

        if self.ssh is not None:
            result['SSH'] = self.ssh.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RDP') is not None:
            temp_model = main_models.GetPolicyResponseBodyPolicyProtocolConfigRDP()
            self.rdp = temp_model.from_map(m.get('RDP'))

        if m.get('SSH') is not None:
            temp_model = main_models.GetPolicyResponseBodyPolicyProtocolConfigSSH()
            self.ssh = temp_model.from_map(m.get('SSH'))

        return self

class GetPolicyResponseBodyPolicyProtocolConfigSSH(DaraModel):
    def __init__(
        self,
        exec_command: str = None,
        sftpchannel: str = None,
        sftpdownload_file: str = None,
        sftpmkdir: str = None,
        sftpremove_file: str = None,
        sftprename_file: str = None,
        sftprmdir: str = None,
        sftpupload_file: str = None,
        sshchannel: str = None,
        x_11forwarding: str = None,
    ):
        # Indicates whether remote command execution is enabled. Valid values:
        # 
        # *   Enable
        # *   Disable
        self.exec_command = exec_command
        # Indicates whether the SFTP channel option is enabled. Valid values:
        # 
        # *   Enable
        # *   Disable
        self.sftpchannel = sftpchannel
        # Indicates whether file downloading is enabled in SFTP-based O\\&M. Valid values:
        # 
        # *   Enable
        # *   Disable
        self.sftpdownload_file = sftpdownload_file
        # Indicates whether folder creation is enabled in SFTP-based O\\&M. Valid values:
        # 
        # *   Enable
        # *   Disable
        self.sftpmkdir = sftpmkdir
        # Indicates whether file deletion is enabled in SFTP-based O\\&M. Valid values:
        # 
        # *   Enable
        # *   Disable
        self.sftpremove_file = sftpremove_file
        # Indicates whether file renaming is enabled in SFTP-based O\\&M. Valid values:
        # 
        # *   Enable
        # *   Disable
        self.sftprename_file = sftprename_file
        # Indicates whether folder deletion is enabled in SFTP-based O\\&M. Valid values:
        # 
        # *   Enable
        # *   Disable
        self.sftprmdir = sftprmdir
        # Indicates whether file uploading is enabled in SFTP-based O\\&M. Valid values:
        # 
        # *   Enable
        # *   Disable
        self.sftpupload_file = sftpupload_file
        # Indicates whether the SSH channel option is enabled. Valid values:
        # 
        # *   Enable
        # *   Disable
        self.sshchannel = sshchannel
        # Indicates whether X11 forwarding is enabled. Valid values:
        # 
        # *   Enable
        # *   Disable
        self.x_11forwarding = x_11forwarding

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.exec_command is not None:
            result['ExecCommand'] = self.exec_command

        if self.sftpchannel is not None:
            result['SFTPChannel'] = self.sftpchannel

        if self.sftpdownload_file is not None:
            result['SFTPDownloadFile'] = self.sftpdownload_file

        if self.sftpmkdir is not None:
            result['SFTPMkdir'] = self.sftpmkdir

        if self.sftpremove_file is not None:
            result['SFTPRemoveFile'] = self.sftpremove_file

        if self.sftprename_file is not None:
            result['SFTPRenameFile'] = self.sftprename_file

        if self.sftprmdir is not None:
            result['SFTPRmdir'] = self.sftprmdir

        if self.sftpupload_file is not None:
            result['SFTPUploadFile'] = self.sftpupload_file

        if self.sshchannel is not None:
            result['SSHChannel'] = self.sshchannel

        if self.x_11forwarding is not None:
            result['X11Forwarding'] = self.x_11forwarding

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExecCommand') is not None:
            self.exec_command = m.get('ExecCommand')

        if m.get('SFTPChannel') is not None:
            self.sftpchannel = m.get('SFTPChannel')

        if m.get('SFTPDownloadFile') is not None:
            self.sftpdownload_file = m.get('SFTPDownloadFile')

        if m.get('SFTPMkdir') is not None:
            self.sftpmkdir = m.get('SFTPMkdir')

        if m.get('SFTPRemoveFile') is not None:
            self.sftpremove_file = m.get('SFTPRemoveFile')

        if m.get('SFTPRenameFile') is not None:
            self.sftprename_file = m.get('SFTPRenameFile')

        if m.get('SFTPRmdir') is not None:
            self.sftprmdir = m.get('SFTPRmdir')

        if m.get('SFTPUploadFile') is not None:
            self.sftpupload_file = m.get('SFTPUploadFile')

        if m.get('SSHChannel') is not None:
            self.sshchannel = m.get('SSHChannel')

        if m.get('X11Forwarding') is not None:
            self.x_11forwarding = m.get('X11Forwarding')

        return self

class GetPolicyResponseBodyPolicyProtocolConfigRDP(DaraModel):
    def __init__(
        self,
        clipboard_download: str = None,
        clipboard_upload: str = None,
        disk_redirection: str = None,
        record_keyboard: str = None,
    ):
        # Indicates whether downloading from the clipboard is enabled. Valid values:
        # 
        # *   Enable
        # *   Disable
        self.clipboard_download = clipboard_download
        # Indicates whether file uploading from the clipboard is enabled. Valid values:
        # 
        # *   Enable
        # *   Disable
        self.clipboard_upload = clipboard_upload
        # Indicates whether driver mapping is enabled. Valid values:
        # 
        # *   Enable
        # *   Disable
        self.disk_redirection = disk_redirection
        # Indicates whether keyboard recording is enabled. Valid values:
        # 
        # *   Enable
        # *   Disable
        self.record_keyboard = record_keyboard

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.clipboard_download is not None:
            result['ClipboardDownload'] = self.clipboard_download

        if self.clipboard_upload is not None:
            result['ClipboardUpload'] = self.clipboard_upload

        if self.disk_redirection is not None:
            result['DiskRedirection'] = self.disk_redirection

        if self.record_keyboard is not None:
            result['RecordKeyboard'] = self.record_keyboard

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClipboardDownload') is not None:
            self.clipboard_download = m.get('ClipboardDownload')

        if m.get('ClipboardUpload') is not None:
            self.clipboard_upload = m.get('ClipboardUpload')

        if m.get('DiskRedirection') is not None:
            self.disk_redirection = m.get('DiskRedirection')

        if m.get('RecordKeyboard') is not None:
            self.record_keyboard = m.get('RecordKeyboard')

        return self

class GetPolicyResponseBodyPolicyIPAclConfig(DaraModel):
    def __init__(
        self,
        acl_type: str = None,
        ips: List[str] = None,
    ):
        # The mode of access control on source IP addresses. Valid values:
        # 
        # *   white: whitelist mode.
        # *   black: blacklist mode.
        self.acl_type = acl_type
        # The IP addresses from which logons are not allowed.
        self.ips = ips

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acl_type is not None:
            result['AclType'] = self.acl_type

        if self.ips is not None:
            result['IPs'] = self.ips

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclType') is not None:
            self.acl_type = m.get('AclType')

        if m.get('IPs') is not None:
            self.ips = m.get('IPs')

        return self

class GetPolicyResponseBodyPolicyCommandConfig(DaraModel):
    def __init__(
        self,
        approval: main_models.GetPolicyResponseBodyPolicyCommandConfigApproval = None,
        deny: main_models.GetPolicyResponseBodyPolicyCommandConfigDeny = None,
    ):
        # The details of the command approval settings.
        self.approval = approval
        # The details of the command control setting.
        self.deny = deny

    def validate(self):
        if self.approval:
            self.approval.validate()
        if self.deny:
            self.deny.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.approval is not None:
            result['Approval'] = self.approval.to_map()

        if self.deny is not None:
            result['Deny'] = self.deny.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Approval') is not None:
            temp_model = main_models.GetPolicyResponseBodyPolicyCommandConfigApproval()
            self.approval = temp_model.from_map(m.get('Approval'))

        if m.get('Deny') is not None:
            temp_model = main_models.GetPolicyResponseBodyPolicyCommandConfigDeny()
            self.deny = temp_model.from_map(m.get('Deny'))

        return self

class GetPolicyResponseBodyPolicyCommandConfigDeny(DaraModel):
    def __init__(
        self,
        acl_type: str = None,
        commands: List[str] = None,
    ):
        # The type of command control. Valid values:
        # 
        # *   white: whitelist mode.
        # *   black: blacklist mode.
        self.acl_type = acl_type
        # An array of controlled commands.
        self.commands = commands

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acl_type is not None:
            result['AclType'] = self.acl_type

        if self.commands is not None:
            result['Commands'] = self.commands

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclType') is not None:
            self.acl_type = m.get('AclType')

        if m.get('Commands') is not None:
            self.commands = m.get('Commands')

        return self

class GetPolicyResponseBodyPolicyCommandConfigApproval(DaraModel):
    def __init__(
        self,
        commands: List[str] = None,
    ):
        # An array of commands that can be run only after approval.
        self.commands = commands

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.commands is not None:
            result['Commands'] = self.commands

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Commands') is not None:
            self.commands = m.get('Commands')

        return self

class GetPolicyResponseBodyPolicyApprovalConfig(DaraModel):
    def __init__(
        self,
        switch_status: str = None,
    ):
        # Indicates whether O\\&M approval is enabled in the control policy. Valid values:
        # 
        # *   **On**: O\\&M approval is enabled.
        # *   **Off**: O\\&M approval is disabled.
        self.switch_status = switch_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.switch_status is not None:
            result['SwitchStatus'] = self.switch_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SwitchStatus') is not None:
            self.switch_status = m.get('SwitchStatus')

        return self

class GetPolicyResponseBodyPolicyAccessTimeRangeConfig(DaraModel):
    def __init__(
        self,
        effective_time: List[main_models.GetPolicyResponseBodyPolicyAccessTimeRangeConfigEffectiveTime] = None,
    ):
        # The details of the periods during which logons are allowed.
        self.effective_time = effective_time

    def validate(self):
        if self.effective_time:
            for v1 in self.effective_time:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['EffectiveTime'] = []
        if self.effective_time is not None:
            for k1 in self.effective_time:
                result['EffectiveTime'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.effective_time = []
        if m.get('EffectiveTime') is not None:
            for k1 in m.get('EffectiveTime'):
                temp_model = main_models.GetPolicyResponseBodyPolicyAccessTimeRangeConfigEffectiveTime()
                self.effective_time.append(temp_model.from_map(k1))

        return self

class GetPolicyResponseBodyPolicyAccessTimeRangeConfigEffectiveTime(DaraModel):
    def __init__(
        self,
        days: List[str] = None,
        hours: List[str] = None,
    ):
        # The days of a week on which logons are allowed.
        self.days = days
        # The time periods during which logons are allowed.
        self.hours = hours

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.days is not None:
            result['Days'] = self.days

        if self.hours is not None:
            result['Hours'] = self.hours

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Days') is not None:
            self.days = m.get('Days')

        if m.get('Hours') is not None:
            self.hours = m.get('Hours')

        return self

