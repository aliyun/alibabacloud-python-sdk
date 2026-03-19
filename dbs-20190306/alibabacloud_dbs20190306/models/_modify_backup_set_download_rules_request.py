# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyBackupSetDownloadRulesRequest(DaraModel):
    def __init__(
        self,
        backup_gateway_id: int = None,
        backup_plan_id: str = None,
        backup_set_download_dir: str = None,
        backup_set_download_target_type: str = None,
        backup_set_download_target_type_location: str = None,
        client_token: str = None,
        full_data_format: str = None,
        increment_data_format: str = None,
        open_auto_download: bool = None,
        owner_id: str = None,
    ):
        # The ID of the backup gateway that is used to download the backup set.
        self.backup_gateway_id = backup_gateway_id
        # The ID of the backup schedule.
        # 
        # This parameter is required.
        self.backup_plan_id = backup_plan_id
        # The server directory to which the backup set is downloaded.
        self.backup_set_download_dir = backup_set_download_dir
        # The type of the destination server to which the backup set is downloaded.
        # 
        # > Set the value to agent, which indicates a server on which a backup gateway is installed.
        self.backup_set_download_target_type = backup_set_download_target_type
        # The type of the destination directory to which the backup set is downloaded. This parameter is required if the automatic download feature is enabled. Valid values:
        # 
        # - local
        # 
        # - nas
        # 
        # - ftp
        # 
        # - minio
        # 
        # > Default value: local.
        self.backup_set_download_target_type_location = backup_set_download_target_type_location
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token
        # The format in which the full backup set is downloaded. Valid values:
        # 
        # - Native
        # 
        # - SQL
        # 
        # - CSV
        # 
        # - JSON
        # 
        # > Default value: CSV.
        self.full_data_format = full_data_format
        # The format in which the incremental backup set is downloaded. Valid values:
        # 
        # - Native
        # 
        # - SQL
        # 
        # - CSV
        # 
        # - JSON
        # 
        # > Default value: Native.
        self.increment_data_format = increment_data_format
        # Specifies whether to enable the automatic download feature. Default value: false.
        self.open_auto_download = open_auto_download
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_gateway_id is not None:
            result['BackupGatewayId'] = self.backup_gateway_id

        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id

        if self.backup_set_download_dir is not None:
            result['BackupSetDownloadDir'] = self.backup_set_download_dir

        if self.backup_set_download_target_type is not None:
            result['BackupSetDownloadTargetType'] = self.backup_set_download_target_type

        if self.backup_set_download_target_type_location is not None:
            result['BackupSetDownloadTargetTypeLocation'] = self.backup_set_download_target_type_location

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.full_data_format is not None:
            result['FullDataFormat'] = self.full_data_format

        if self.increment_data_format is not None:
            result['IncrementDataFormat'] = self.increment_data_format

        if self.open_auto_download is not None:
            result['OpenAutoDownload'] = self.open_auto_download

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupGatewayId') is not None:
            self.backup_gateway_id = m.get('BackupGatewayId')

        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')

        if m.get('BackupSetDownloadDir') is not None:
            self.backup_set_download_dir = m.get('BackupSetDownloadDir')

        if m.get('BackupSetDownloadTargetType') is not None:
            self.backup_set_download_target_type = m.get('BackupSetDownloadTargetType')

        if m.get('BackupSetDownloadTargetTypeLocation') is not None:
            self.backup_set_download_target_type_location = m.get('BackupSetDownloadTargetTypeLocation')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('FullDataFormat') is not None:
            self.full_data_format = m.get('FullDataFormat')

        if m.get('IncrementDataFormat') is not None:
            self.increment_data_format = m.get('IncrementDataFormat')

        if m.get('OpenAutoDownload') is not None:
            self.open_auto_download = m.get('OpenAutoDownload')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        return self

