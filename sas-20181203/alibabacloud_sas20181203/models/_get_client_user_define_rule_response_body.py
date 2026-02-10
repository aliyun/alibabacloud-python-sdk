# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class GetClientUserDefineRuleResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        user_define_rule_detail: main_models.GetClientUserDefineRuleResponseBodyUserDefineRuleDetail = None,
    ):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The information about the custom defense rule.
        self.user_define_rule_detail = user_define_rule_detail

    def validate(self):
        if self.user_define_rule_detail:
            self.user_define_rule_detail.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.user_define_rule_detail is not None:
            result['UserDefineRuleDetail'] = self.user_define_rule_detail.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('UserDefineRuleDetail') is not None:
            temp_model = main_models.GetClientUserDefineRuleResponseBodyUserDefineRuleDetail()
            self.user_define_rule_detail = temp_model.from_map(m.get('UserDefineRuleDetail'))

        return self

class GetClientUserDefineRuleResponseBodyUserDefineRuleDetail(DaraModel):
    def __init__(
        self,
        action_type: str = None,
        cmdline: str = None,
        domain: str = None,
        file_path: str = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        ip: str = None,
        id: int = None,
        md_5list: str = None,
        name: str = None,
        new_file_path: str = None,
        parent_cmdline: str = None,
        parent_proc_path: str = None,
        platform: str = None,
        port: int = None,
        port_str: str = None,
        proc_path: str = None,
        registry_content: str = None,
        registry_key: str = None,
        type: int = None,
    ):
        # The action of the custom defense rule. Valid values:
        # 
        # *   **0**: allow
        # *   **1**: block
        self.action_type = action_type
        # The command line.
        self.cmdline = cmdline
        # The domain name.
        self.domain = domain
        # The file path.
        self.file_path = file_path
        # The time when the custom defense rule was created.
        self.gmt_create = gmt_create
        # The time when the custom defense rule was last modified.
        self.gmt_modified = gmt_modified
        # The IP address.
        self.ip = ip
        # The ID of the custom defense rule.
        self.id = id
        # The hash values of processes.
        self.md_5list = md_5list
        # The name of the custom defense rule.
        self.name = name
        # The new file path after the file is renamed.
        self.new_file_path = new_file_path
        # The parent command line.
        self.parent_cmdline = parent_cmdline
        # The path to the parent process.
        self.parent_proc_path = parent_proc_path
        # The type of the operating system. Valid values:
        # 
        # *   **linux**
        # *   **windows**
        # *   **all**
        self.platform = platform
        # The port number.
        self.port = port
        # The port number. Valid values: 1 to 65535.
        self.port_str = port_str
        # The path to the process.
        self.proc_path = proc_path
        # The registry value.
        self.registry_content = registry_content
        # The registry key.
        self.registry_key = registry_key
        # The type of the custom defense rule. Valid values:
        # 
        # *   **1**: Process hash
        # *   **2**: Command line
        # *   **3**: Process Network
        # *   **4**: File Read and Write
        # *   **5**: Operation on Registry
        # *   **6**: Dynamic-link Library Loading
        # *   **7**: File Renaming
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action_type is not None:
            result['ActionType'] = self.action_type

        if self.cmdline is not None:
            result['Cmdline'] = self.cmdline

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.file_path is not None:
            result['FilePath'] = self.file_path

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.ip is not None:
            result['IP'] = self.ip

        if self.id is not None:
            result['Id'] = self.id

        if self.md_5list is not None:
            result['Md5List'] = self.md_5list

        if self.name is not None:
            result['Name'] = self.name

        if self.new_file_path is not None:
            result['NewFilePath'] = self.new_file_path

        if self.parent_cmdline is not None:
            result['ParentCmdline'] = self.parent_cmdline

        if self.parent_proc_path is not None:
            result['ParentProcPath'] = self.parent_proc_path

        if self.platform is not None:
            result['Platform'] = self.platform

        if self.port is not None:
            result['Port'] = self.port

        if self.port_str is not None:
            result['PortStr'] = self.port_str

        if self.proc_path is not None:
            result['ProcPath'] = self.proc_path

        if self.registry_content is not None:
            result['RegistryContent'] = self.registry_content

        if self.registry_key is not None:
            result['RegistryKey'] = self.registry_key

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionType') is not None:
            self.action_type = m.get('ActionType')

        if m.get('Cmdline') is not None:
            self.cmdline = m.get('Cmdline')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('IP') is not None:
            self.ip = m.get('IP')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Md5List') is not None:
            self.md_5list = m.get('Md5List')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NewFilePath') is not None:
            self.new_file_path = m.get('NewFilePath')

        if m.get('ParentCmdline') is not None:
            self.parent_cmdline = m.get('ParentCmdline')

        if m.get('ParentProcPath') is not None:
            self.parent_proc_path = m.get('ParentProcPath')

        if m.get('Platform') is not None:
            self.platform = m.get('Platform')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('PortStr') is not None:
            self.port_str = m.get('PortStr')

        if m.get('ProcPath') is not None:
            self.proc_path = m.get('ProcPath')

        if m.get('RegistryContent') is not None:
            self.registry_content = m.get('RegistryContent')

        if m.get('RegistryKey') is not None:
            self.registry_key = m.get('RegistryKey')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

