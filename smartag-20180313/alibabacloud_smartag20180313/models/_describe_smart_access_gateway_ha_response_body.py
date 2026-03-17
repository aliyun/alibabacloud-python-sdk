# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_smartag20180313 import models as main_models
from darabonba.model import DaraModel

class DescribeSmartAccessGatewayHaResponseBody(DaraModel):
    def __init__(
        self,
        backup_device_id: str = None,
        device_level_backup_state: str = None,
        device_level_backup_type: str = None,
        link_backup_info_list: main_models.DescribeSmartAccessGatewayHaResponseBodyLinkBackupInfoList = None,
        main_device_id: str = None,
        request_id: str = None,
        smart_agid: str = None,
    ):
        # The serial number of the standby SAG device.
        self.backup_device_id = backup_device_id
        # Indicates whether device-based HA is enabled. Valid values:
        # 
        # *   **ON**: enabled
        # *   **OFF**: disabled
        self.device_level_backup_state = device_level_backup_state
        # The deployment mode of the SAG devices that have HA enabled. Valid values:
        # 
        # *   **warm_backup**: active-active mode.
        # *   **cold_backup**: active-standby mode.
        # *   **no_backup**: HA is disabled.
        self.device_level_backup_type = device_level_backup_type
        self.link_backup_info_list = link_backup_info_list
        # The serial number of the active SAG device.
        self.main_device_id = main_device_id
        # The ID of the request.
        self.request_id = request_id
        # The ID of the SAG instance.
        self.smart_agid = smart_agid

    def validate(self):
        if self.link_backup_info_list:
            self.link_backup_info_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_device_id is not None:
            result['BackupDeviceId'] = self.backup_device_id

        if self.device_level_backup_state is not None:
            result['DeviceLevelBackupState'] = self.device_level_backup_state

        if self.device_level_backup_type is not None:
            result['DeviceLevelBackupType'] = self.device_level_backup_type

        if self.link_backup_info_list is not None:
            result['LinkBackupInfoList'] = self.link_backup_info_list.to_map()

        if self.main_device_id is not None:
            result['MainDeviceId'] = self.main_device_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.smart_agid is not None:
            result['SmartAGId'] = self.smart_agid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupDeviceId') is not None:
            self.backup_device_id = m.get('BackupDeviceId')

        if m.get('DeviceLevelBackupState') is not None:
            self.device_level_backup_state = m.get('DeviceLevelBackupState')

        if m.get('DeviceLevelBackupType') is not None:
            self.device_level_backup_type = m.get('DeviceLevelBackupType')

        if m.get('LinkBackupInfoList') is not None:
            temp_model = main_models.DescribeSmartAccessGatewayHaResponseBodyLinkBackupInfoList()
            self.link_backup_info_list = temp_model.from_map(m.get('LinkBackupInfoList'))

        if m.get('MainDeviceId') is not None:
            self.main_device_id = m.get('MainDeviceId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SmartAGId') is not None:
            self.smart_agid = m.get('SmartAGId')

        return self

class DescribeSmartAccessGatewayHaResponseBodyLinkBackupInfoList(DaraModel):
    def __init__(
        self,
        link_backup_info_list: List[main_models.DescribeSmartAccessGatewayHaResponseBodyLinkBackupInfoListLinkBackupInfoList] = None,
    ):
        self.link_backup_info_list = link_backup_info_list

    def validate(self):
        if self.link_backup_info_list:
            for v1 in self.link_backup_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['LinkBackupInfoList'] = []
        if self.link_backup_info_list is not None:
            for k1 in self.link_backup_info_list:
                result['LinkBackupInfoList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.link_backup_info_list = []
        if m.get('LinkBackupInfoList') is not None:
            for k1 in m.get('LinkBackupInfoList'):
                temp_model = main_models.DescribeSmartAccessGatewayHaResponseBodyLinkBackupInfoListLinkBackupInfoList()
                self.link_backup_info_list.append(temp_model.from_map(k1))

        return self

class DescribeSmartAccessGatewayHaResponseBodyLinkBackupInfoListLinkBackupInfoList(DaraModel):
    def __init__(
        self,
        backup_link_id: str = None,
        backup_link_state: str = None,
        link_level_backup_state: str = None,
        link_level_backup_type: str = None,
        main_link_id: str = None,
        main_link_state: str = None,
    ):
        self.backup_link_id = backup_link_id
        self.backup_link_state = backup_link_state
        self.link_level_backup_state = link_level_backup_state
        self.link_level_backup_type = link_level_backup_type
        self.main_link_id = main_link_id
        self.main_link_state = main_link_state

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_link_id is not None:
            result['BackupLinkId'] = self.backup_link_id

        if self.backup_link_state is not None:
            result['BackupLinkState'] = self.backup_link_state

        if self.link_level_backup_state is not None:
            result['LinkLevelBackupState'] = self.link_level_backup_state

        if self.link_level_backup_type is not None:
            result['LinkLevelBackupType'] = self.link_level_backup_type

        if self.main_link_id is not None:
            result['MainLinkId'] = self.main_link_id

        if self.main_link_state is not None:
            result['MainLinkState'] = self.main_link_state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupLinkId') is not None:
            self.backup_link_id = m.get('BackupLinkId')

        if m.get('BackupLinkState') is not None:
            self.backup_link_state = m.get('BackupLinkState')

        if m.get('LinkLevelBackupState') is not None:
            self.link_level_backup_state = m.get('LinkLevelBackupState')

        if m.get('LinkLevelBackupType') is not None:
            self.link_level_backup_type = m.get('LinkLevelBackupType')

        if m.get('MainLinkId') is not None:
            self.main_link_id = m.get('MainLinkId')

        if m.get('MainLinkState') is not None:
            self.main_link_state = m.get('MainLinkState')

        return self

