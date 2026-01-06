# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_hbr20170908 import models as main_models
from darabonba.model import DaraModel

class DescribeHanaBackupSettingResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        hana_backup_setting: main_models.DescribeHanaBackupSettingResponseBodyHanaBackupSetting = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code. The status code 200 indicates that the call is successful.
        self.code = code
        # The backup settings.
        self.hana_backup_setting = hana_backup_setting
        # The message that is returned. If the call is successful, "successful" is returned. If the call fails, an error message is returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the call is successful. Valid values:
        # 
        # *   true: The call is successful.
        # *   false: The call fails.
        self.success = success

    def validate(self):
        if self.hana_backup_setting:
            self.hana_backup_setting.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.hana_backup_setting is not None:
            result['HanaBackupSetting'] = self.hana_backup_setting.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HanaBackupSetting') is not None:
            temp_model = main_models.DescribeHanaBackupSettingResponseBodyHanaBackupSetting()
            self.hana_backup_setting = temp_model.from_map(m.get('HanaBackupSetting'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeHanaBackupSettingResponseBodyHanaBackupSetting(DaraModel):
    def __init__(
        self,
        catalog_backup_parameter_file: str = None,
        catalog_backup_using_backint: bool = None,
        data_backup_parameter_file: str = None,
        database_name: str = None,
        enable_auto_log_backup: bool = None,
        log_backup_parameter_file: str = None,
        log_backup_timeout: int = None,
        log_backup_using_backint: bool = None,
    ):
        # The configuration file for catalog backup.
        self.catalog_backup_parameter_file = catalog_backup_parameter_file
        # Indicates whether Backint is used to back up catalogs. Valid values:
        # 
        # *   true: Backint is used to back up catalogs.
        # *   false: Backint is not used to back up catalogs.
        self.catalog_backup_using_backint = catalog_backup_using_backint
        # The configuration file for data backup.
        self.data_backup_parameter_file = data_backup_parameter_file
        # The name of the database.
        self.database_name = database_name
        # Indicates whether automatic log backup is enabled. Valid values:
        # 
        # *   **true**: Automatic log backup is enabled.
        # *   **false**: Automatic log backup is disabled.
        self.enable_auto_log_backup = enable_auto_log_backup
        # The configuration file for log backup.
        self.log_backup_parameter_file = log_backup_parameter_file
        # The interval at which logs are backed up. Unit: seconds.
        self.log_backup_timeout = log_backup_timeout
        # Indicates whether Backint is used to back up logs. Valid values:
        # 
        # *   true: Backint is used to back up logs.
        # *   false: Backint is not used to back up logs.
        self.log_backup_using_backint = log_backup_using_backint

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.catalog_backup_parameter_file is not None:
            result['CatalogBackupParameterFile'] = self.catalog_backup_parameter_file

        if self.catalog_backup_using_backint is not None:
            result['CatalogBackupUsingBackint'] = self.catalog_backup_using_backint

        if self.data_backup_parameter_file is not None:
            result['DataBackupParameterFile'] = self.data_backup_parameter_file

        if self.database_name is not None:
            result['DatabaseName'] = self.database_name

        if self.enable_auto_log_backup is not None:
            result['EnableAutoLogBackup'] = self.enable_auto_log_backup

        if self.log_backup_parameter_file is not None:
            result['LogBackupParameterFile'] = self.log_backup_parameter_file

        if self.log_backup_timeout is not None:
            result['LogBackupTimeout'] = self.log_backup_timeout

        if self.log_backup_using_backint is not None:
            result['LogBackupUsingBackint'] = self.log_backup_using_backint

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogBackupParameterFile') is not None:
            self.catalog_backup_parameter_file = m.get('CatalogBackupParameterFile')

        if m.get('CatalogBackupUsingBackint') is not None:
            self.catalog_backup_using_backint = m.get('CatalogBackupUsingBackint')

        if m.get('DataBackupParameterFile') is not None:
            self.data_backup_parameter_file = m.get('DataBackupParameterFile')

        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')

        if m.get('EnableAutoLogBackup') is not None:
            self.enable_auto_log_backup = m.get('EnableAutoLogBackup')

        if m.get('LogBackupParameterFile') is not None:
            self.log_backup_parameter_file = m.get('LogBackupParameterFile')

        if m.get('LogBackupTimeout') is not None:
            self.log_backup_timeout = m.get('LogBackupTimeout')

        if m.get('LogBackupUsingBackint') is not None:
            self.log_backup_using_backint = m.get('LogBackupUsingBackint')

        return self

