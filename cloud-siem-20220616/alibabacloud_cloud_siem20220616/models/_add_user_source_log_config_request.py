# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddUserSourceLogConfigRequest(DaraModel):
    def __init__(
        self,
        deleted: int = None,
        dis_play_line: str = None,
        region_id: str = None,
        source_log_code: str = None,
        source_log_info: str = None,
        source_prod_code: str = None,
        sub_user_id: int = None,
    ):
        # Specifies whether to add or delete the log collection task. Valid values:
        # 
        # - -1: Deletes the task.
        # 
        # - 0: Adds the task.
        self.deleted = deleted
        # The detailed information about the SLS log to be collected.
        self.dis_play_line = dis_play_line
        # The region where the Data Management center of Threat Analysis is located. Select a region based on the region where your assets reside. Valid values:
        # 
        # - cn-hangzhou: Your assets are in the Chinese mainland or Hong Kong (China).
        # 
        # - ap-southeast-1: Your assets are in regions outside China.
        self.region_id = region_id
        # The code of the log.
        self.source_log_code = source_log_code
        # The detailed information about the Simple Log Service (SLS) log to be collected. The value is a JSON string.
        # 
        # This parameter is required.
        self.source_log_info = source_log_info
        # The code of the product.
        self.source_prod_code = source_prod_code
        # The ID of the Alibaba Cloud account for which you want to collect logs.
        # 
        # This parameter is required.
        self.sub_user_id = sub_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.deleted is not None:
            result['Deleted'] = self.deleted

        if self.dis_play_line is not None:
            result['DisPlayLine'] = self.dis_play_line

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.source_log_code is not None:
            result['SourceLogCode'] = self.source_log_code

        if self.source_log_info is not None:
            result['SourceLogInfo'] = self.source_log_info

        if self.source_prod_code is not None:
            result['SourceProdCode'] = self.source_prod_code

        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')

        if m.get('DisPlayLine') is not None:
            self.dis_play_line = m.get('DisPlayLine')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SourceLogCode') is not None:
            self.source_log_code = m.get('SourceLogCode')

        if m.get('SourceLogInfo') is not None:
            self.source_log_info = m.get('SourceLogInfo')

        if m.get('SourceProdCode') is not None:
            self.source_prod_code = m.get('SourceProdCode')

        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')

        return self

