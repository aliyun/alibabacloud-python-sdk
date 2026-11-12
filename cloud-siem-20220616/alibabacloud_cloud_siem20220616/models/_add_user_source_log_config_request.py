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
        # Specifies the ingestion action. Valid values:
        # - -1: Deletes the ingestion.
        # - 0: Adds the ingestion.
        self.deleted = deleted
        # The detailed Simple Log Service (SLS) information for log ingestion.
        self.dis_play_line = dis_play_line
        # The region where the data management center of Threat Analysis is located. Select the region of the management center based on the region of your assets. Valid values:
        # - cn-hangzhou: The assets are located in the Chinese mainland and Hong Kong (China).
        # - ap-southeast-1: The assets are located outside China.
        self.region_id = region_id
        # The log code.
        self.source_log_code = source_log_code
        # The detailed Simple Log Service (SLS) information for log ingestion in JSON format.
        # 
        # This parameter is required.
        self.source_log_info = source_log_info
        # The product code.
        self.source_prod_code = source_prod_code
        # The Alibaba Cloud account ID for log ingestion.
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

