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
        project_id: int = None,
        protocol_config: main_models.SetPolicyProtocolConfigRequestProtocolConfig = None,
        region_id: str = None,
    ):
        # The instance ID of the bastion host.
        # > You can invoke [DescribeInstances](https://help.aliyun.com/document_detail/153281.html) to obtain this parameter.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the control policy to modify.
        # 
        # > You can call [ListPolicies](https://help.aliyun.com/document_detail/2758876.html) to obtain this parameter.
        # 
        # This parameter is required.
        self.policy_id = policy_id
        # The project ID.
        self.project_id = project_id
        # The protocol control configuration.
        # 
        # This parameter is required.
        self.protocol_config = protocol_config
        # The region ID of the bastion host.
        # > For the mapping between region IDs and region names, see [Regions and zones](https://help.aliyun.com/document_detail/40654.html).
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

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

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

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

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
        # The RDP option configuration details.
        self.rdp = rdp
        # The SSH and SFTP option configuration details.
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
        tcp_forwarding: str = None,
        x_11forwarding: str = None,
    ):
        # Specifies whether to allow direct TCP connection.
        self.allow_direct_tcp = allow_direct_tcp
        # Specifies whether to allow TCP forwarding.
        self.allow_tcp_forwarding = allow_tcp_forwarding
        # The remote command execution configuration. Valid values:
        # 
        # - Enable: Enabled.
        # - Disable: Disabled.
        # > If this parameter is not specified, the default value is Disable.
        self.exec_command = exec_command
        # The SFTP channel configuration. Valid values:
        # 
        # - Enable: Enabled.
        # - Disable: Disabled.
        # 
        # > - If this parameter is not specified, the default value is Disable.
        # > - At least one of the SSH channel and SFTP channel must be set to Enable.
        # > - If you enable the SFTP-only permission for a host account, do not disable both the SSH channel and SFTP channel for that account in the control policy. Otherwise, you cannot use the host account to access the target server through the bastion host.
        self.sftpchannel = sftpchannel
        # The SFTP file download configuration. Valid values:
        # 
        # - Enable: Enabled.
        # - Disable: Disabled.
        # > If this parameter is not specified, the default value is Disable.
        self.sftpdownload_file = sftpdownload_file
        # The SFTP folder creation configuration. Valid values:
        # 
        # - Enable: Enabled.
        # - Disable: Disabled.
        # > If this parameter is not specified, the default value is Disable.
        self.sftpmkdir = sftpmkdir
        # The SFTP file deletion configuration. Valid values:
        # 
        # - Enable: Enabled.
        # - Disable: Disabled.
        # > If this parameter is not specified, the default value is Disable.
        self.sftpremove_file = sftpremove_file
        # The SFTP file rename configuration. Valid values:
        # 
        # - Enable: Enabled.
        # - Disable: Disabled.
        # > If this parameter is not specified, the default value is Disable.
        self.sftprename_file = sftprename_file
        # The SFTP folder deletion configuration. Valid values:
        # 
        # - Enable: Enabled.
        # - Disable: Disabled.
        # > If this parameter is not specified, the default value is Disable.
        self.sftprmdir = sftprmdir
        # The SFTP file upload configuration. Valid values:
        # 
        # - Enable: Enabled.
        # - Disable: Disabled.
        # > If this parameter is not specified, the default value is Disable.
        self.sftpupload_file = sftpupload_file
        # The SSH channel configuration. Valid values:
        # 
        # - Enable: Enabled.
        # - Disable: Disabled.
        # 
        # > - If this parameter is not specified, the default value is Disable.
        # > - At least one of the SSH channel and SFTP channel must be set to Enable. If the SSH channel is set to Disable, you cannot log on to asset accounts by using SSH permissions. Proceed with caution.
        # > - If you enable the SFTP-only permission for a host account, do not disable both the SSH channel and SFTP channel for that account in the control policy. Otherwise, you cannot use the host account to access the target server through the bastion host.
        self.sshchannel = sshchannel
        # Specifies whether to allow TCP forwarding.
        self.tcp_forwarding = tcp_forwarding
        # The X11 forwarding configuration. Valid values:
        # 
        # - Enable: Enabled.
        # - Disable: Disabled.
        # > If this parameter is not specified, the default value is Disable.
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

        if self.tcp_forwarding is not None:
            result['TcpForwarding'] = self.tcp_forwarding

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

        if m.get('TcpForwarding') is not None:
            self.tcp_forwarding = m.get('TcpForwarding')

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
        # The clipboard download configuration. Valid values:
        # 
        # - Enable: Enabled.
        # - Disable: Disabled.
        # 
        # > If this parameter is not specified, the default value is Disable.
        self.clipboard_download = clipboard_download
        # The clipboard upload configuration. Valid values:
        # 
        # - Enable: Enabled.
        # - Disable: Disabled.
        # > If this parameter is not specified, the default value is Disable.
        self.clipboard_upload = clipboard_upload
        # The drive/printer mapping configuration. Valid values:
        # 
        # - Enable: Enabled.
        # - Disable: Disabled.
        # > If this parameter is not specified, the default value is Disable.
        self.disk_redirection = disk_redirection
        # Specifies whether to allow disk download.
        self.disk_redirection_download = disk_redirection_download
        # Specifies whether to allow disk upload.
        self.disk_redirection_upload = disk_redirection_upload
        # The keyboard recording configuration. Valid values:
        # 
        # - Enable: Enabled.
        # - Disable: Disabled.
        # > If this parameter is not specified, the default value is Disable.
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

