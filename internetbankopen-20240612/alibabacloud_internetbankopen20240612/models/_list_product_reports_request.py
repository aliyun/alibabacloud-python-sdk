# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListProductReportsRequest(DaraModel):
    def __init__(
        self,
        latest_only: bool = None,
        product_code: str = None,
    ):
        # Specifies whether to return only the most recent active epoch report. If this parameter is omitted or set to false, the operation returns active reports within the last ten completed natural weeks in UTC+8, up to ten records. If set to true, the operation queries the most recent active report from all completed historical epochs, returning at most one record without the ten-week limit. Only true or false is accepted. If a string is passed, it must strictly use the lowercase characters true or false. Other values return InvalidParameter.LatestOnly. This operation does not support paging.
        self.latest_only = latest_only
        # The product code of the data product for which to query periodic reports. This must be consistent with the product code used when calling InvokeDataProduct. This parameter is required and allows only 1 to 128 ASCII letters, digits, periods (.), underscores (_), or hyphens (-). Leading and trailing spaces are not trimmed. If this parameter is missing or incorrectly formatted, InvalidParameter.ProductCode is returned. The query is limited to reports belonging to the current Alibaba Cloud account. If no available reports exist, an empty Reports array is returned.
        # 
        # This parameter is required.
        self.product_code = product_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.latest_only is not None:
            result['LatestOnly'] = self.latest_only

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LatestOnly') is not None:
            self.latest_only = m.get('LatestOnly')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        return self

