# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class ListFileProtectPluginStatusResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListFileProtectPluginStatusResponseBodyData] = None,
        page_info: main_models.ListFileProtectPluginStatusResponseBodyPageInfo = None,
        request_id: str = None,
    ):
        # The data returned if the call is successful.
        self.data = data
        # The pagination information.
        self.page_info = page_info
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListFileProtectPluginStatusResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('PageInfo') is not None:
            temp_model = main_models.ListFileProtectPluginStatusResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListFileProtectPluginStatusResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The page number.
        self.current_page = current_page
        # The number of entries per page.
        self.page_size = page_size
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListFileProtectPluginStatusResponseBodyData(DaraModel):
    def __init__(
        self,
        client_version: str = None,
        install_code: str = None,
        install_message: str = None,
        installed: bool = None,
        instance_name: str = None,
        internet_ip: str = None,
        intranet_ip: str = None,
        online: bool = None,
        platform: str = None,
        support_file: bool = None,
        uuid: str = None,
    ):
        # The version of the Security Center agent.
        self.client_version = client_version
        # The returned code after you install the Security Center agent. Valid values:
        # 
        # 1.  0: The installation is successful.
        # 2.  \\-2: The kernel does not support the installation.
        self.install_code = install_code
        # The returned message after you install the Security Center agent.
        self.install_message = install_message
        # Indicates whether the Security Center agent is installed.
        self.installed = installed
        # The name of the instance.
        self.instance_name = instance_name
        # The public IP address that is associated with the instance.
        self.internet_ip = internet_ip
        # The private IP address that is associated with the instance.
        self.intranet_ip = intranet_ip
        # Indicates whether the Security Center agent is online. Valid value:
        # 
        # *   **true**
        # *   **false**
        self.online = online
        # The type of the operating system. Valid values:
        # 
        # *   **windows**: Windows
        # *   **linux**: Linux
        self.platform = platform
        # Indicates whether the core file monitoring file is supported.
        self.support_file = support_file
        # The UUID of the asset.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_version is not None:
            result['ClientVersion'] = self.client_version

        if self.install_code is not None:
            result['InstallCode'] = self.install_code

        if self.install_message is not None:
            result['InstallMessage'] = self.install_message

        if self.installed is not None:
            result['Installed'] = self.installed

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip

        if self.intranet_ip is not None:
            result['IntranetIp'] = self.intranet_ip

        if self.online is not None:
            result['Online'] = self.online

        if self.platform is not None:
            result['Platform'] = self.platform

        if self.support_file is not None:
            result['SupportFile'] = self.support_file

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientVersion') is not None:
            self.client_version = m.get('ClientVersion')

        if m.get('InstallCode') is not None:
            self.install_code = m.get('InstallCode')

        if m.get('InstallMessage') is not None:
            self.install_message = m.get('InstallMessage')

        if m.get('Installed') is not None:
            self.installed = m.get('Installed')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')

        if m.get('IntranetIp') is not None:
            self.intranet_ip = m.get('IntranetIp')

        if m.get('Online') is not None:
            self.online = m.get('Online')

        if m.get('Platform') is not None:
            self.platform = m.get('Platform')

        if m.get('SupportFile') is not None:
            self.support_file = m.get('SupportFile')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

