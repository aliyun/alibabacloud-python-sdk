# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_yundun_bastionhost20191209 import models as main_models
from darabonba.model import DaraModel

class SetPolicyProtocolConfigRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        policy_id: str = None,
        protocol_config: main_models.SetPolicyProtocolConfigRequestProtocolConfig = None,
        region_id: str = None,
    ):
        # The bastion host ID.
        # 
        # > You can call the [DescribeInstances](https://help.aliyun.com/document_detail/153281.html) operation to query the bastion host ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the control policy that you want to modify.
        # 
        # > You can call the [ListPolicies](https://help.aliyun.com/document_detail/2758876.html) operation to query the control policy ID.
        # 
        # This parameter is required.
        self.policy_id = policy_id
        # The protocol control settings.
        # 
        # This parameter is required.
        self.protocol_config = protocol_config
        # The region ID of the bastion host.
        # 
        # > For more information about the mapping between region IDs and region names, see [Regions and zones](https://help.aliyun.com/document_detail/40654.html).
        self.region_id = region_id

    def validate(self):
        if self.protocol_config:
            self.protocol_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id

        if self.protocol_config is not None:
            result['ProtocolConfig'] = self.protocol_config.to_map()

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')

        if m.get('ProtocolConfig') is not None:
            temp_model = main_models.SetPolicyProtocolConfigRequestProtocolConfig()
            self.protocol_config = temp_model.from_map(m.get('ProtocolConfig'))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

class SetPolicyProtocolConfigRequestProtocolConfig(DaraModel):
    def __init__(
        self,
        rdp: main_models.SetPolicyProtocolConfigRequestProtocolConfigRDP = None,
        ssh: main_models.SetPolicyProtocolConfigRequestProtocolConfigSSH = None,
    ):
        # The settings of the Remote Desktop Protocol (RDP) options.
        self.rdp = rdp
        # The settings of the SSH and SSH Fine Transfer Protocol (SFTP) options.
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
            temp_model = main_models.SetPolicyProtocolConfigRequestProtocolConfigRDP()
            self.rdp = temp_model.from_map(m.get('RDP'))

        if m.get('SSH') is not None:
            temp_model = main_models.SetPolicyProtocolConfigRequestProtocolConfigSSH()
            self.ssh = temp_model.from_map(m.get('SSH'))

        return self

class SetPolicyProtocolConfigRequestProtocolConfigSSH(DaraModel):
    def __init__(
        self,
        allow_direct_tcp: str = None,
        allow_tcp_forwarding: str = None,
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
        self.allow_direct_tcp = allow_direct_tcp
        self.allow_tcp_forwarding = allow_tcp_forwarding
        # Specifies whether to enable remote command execution. Valid values:
        # 
        # *   Enable
        # *   Disable
        # 
        # > If you do not specify this parameter, the default value Disable is used.
        self.exec_command = exec_command
        # Specifies whether to enable SFTP channels. Valid values:
        # 
        # *   Enable
        # *   Disable
        # 
        # > 
        # 
        # *   If you do not specify this parameter, the default value Disable is used.
        # 
        # *   You must set at least one of the following parameters to Enable: SSHChannel and SFTPChannel.
        # 
        # *   If you select Enable Only SFTP Permission for a host account, do not set SSHChannel and SFTPChannel to Disable for the account. Otherwise, users of the bastion host cannot use the account to access the host.
        self.sftpchannel = sftpchannel
        # Specifies whether to enable file downloading during SFTP-based O\\&M. Valid values:
        # 
        # *   Enable
        # *   Disable
        # 
        # > If you do not specify this parameter, the default value Disable is used.
        self.sftpdownload_file = sftpdownload_file
        # Specifies whether to enable folder creation during SFTP-based O\\&M. Valid values:
        # 
        # *   Enable
        # *   Disable
        # 
        # > If you do not specify this parameter, the default value Disable is used.
        self.sftpmkdir = sftpmkdir
        # Specifies whether to enable file deletion during SFTP-based O\\&M. Valid values:
        # 
        # *   Enable
        # *   Disable
        # 
        # > If you do not specify this parameter, the default value Disable is used.
        self.sftpremove_file = sftpremove_file
        # Specifies whether to enable file renaming during SFTP-based O\\&M. Valid values:
        # 
        # *   Enable
        # *   Disable
        # 
        # > If you do not specify this parameter, the default value Disable is used.
        self.sftprename_file = sftprename_file
        # Specifies whether to enable folder deletion during SFTP-based O\\&M. Valid values:
        # 
        # *   Enable
        # *   Disable
        # 
        # > If you do not specify this parameter, the default value Disable is used.
        self.sftprmdir = sftprmdir
        # Specifies whether to enable file uploading during SFTP-based O\\&M. Valid values:
        # 
        # *   Enable
        # *   Disable
        # 
        # > If you do not specify this parameter, the default value Disable is used.
        self.sftpupload_file = sftpupload_file
        # Specifies whether to enable SSH channels. Valid values:
        # 
        # *   Enable
        # *   Disable
        # 
        # > 
        # 
        # *   If you do not specify this parameter, the default value Disable is used.
        # 
        # *   You must set at least one of the following parameters to Enable: SSHChannel and SFTPChannel. If you set SSHChannel to Disable, SSH-based logon is disabled for the asset account. Proceed with caution.
        # 
        # *   If you select Enable Only SFTP Permission for a host account, do not set SSHChannel and SFTPChannel to Disable for the account. Otherwise, users of the bastion host cannot use the account to access the host.
        self.sshchannel = sshchannel
        # Specifies whether to enable X11 forwarding. Valid values:
        # 
        # *   Enable
        # *   Disable
        # 
        # > If you do not specify this parameter, the default value Disable is used.
        self.x_11forwarding = x_11forwarding

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allow_direct_tcp is not None:
            result['AllowDirectTcp'] = self.allow_direct_tcp

        if self.allow_tcp_forwarding is not None:
            result['AllowTcpForwarding'] = self.allow_tcp_forwarding

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
        if m.get('AllowDirectTcp') is not None:
            self.allow_direct_tcp = m.get('AllowDirectTcp')

        if m.get('AllowTcpForwarding') is not None:
            self.allow_tcp_forwarding = m.get('AllowTcpForwarding')

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

class SetPolicyProtocolConfigRequestProtocolConfigRDP(DaraModel):
    def __init__(
        self,
        clipboard_download: str = None,
        clipboard_upload: str = None,
        disk_redirection: str = None,
        disk_redirection_download: str = None,
        disk_redirection_upload: str = None,
        record_keyboard: str = None,
    ):
        # Specifies whether to enable downloading from the clipboard. Valid values:
        # 
        # *   Enable
        # *   Disable
        # 
        # > If you do not specify this parameter, the default value Disable is used.
        self.clipboard_download = clipboard_download
        # Specifies whether to enable uploading from the clipboard. Valid values:
        # 
        # *   Enable
        # *   Disable
        # 
        # > If you do not specify this parameter, the default value Disable is used.
        self.clipboard_upload = clipboard_upload
        # Specifies whether to enable driver mapping. Valid values:
        # 
        # *   Enable
        # *   Disable
        # 
        # > If you do not specify this parameter, the default value Disable is used.
        self.disk_redirection = disk_redirection
        self.disk_redirection_download = disk_redirection_download
        self.disk_redirection_upload = disk_redirection_upload
        # Specifies whether to enable keyboard operation recording. Valid values:
        # 
        # *   Enable
        # *   Disable
        # 
        # > If you do not specify this parameter, the default value Disable is used.
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

        if self.disk_redirection_download is not None:
            result['DiskRedirectionDownload'] = self.disk_redirection_download

        if self.disk_redirection_upload is not None:
            result['DiskRedirectionUpload'] = self.disk_redirection_upload

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

        if m.get('DiskRedirectionDownload') is not None:
            self.disk_redirection_download = m.get('DiskRedirectionDownload')

        if m.get('DiskRedirectionUpload') is not None:
            self.disk_redirection_upload = m.get('DiskRedirectionUpload')

        if m.get('RecordKeyboard') is not None:
            self.record_keyboard = m.get('RecordKeyboard')

        return self

