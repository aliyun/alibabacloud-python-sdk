# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSupportFeaturesResponseBody(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        request_id: str = None,
        support_feature_list: str = None,
    ):
        # The ID of the instance.
        self.dbinstance_id = dbinstance_id
        # The ID of the request.
        self.request_id = request_id
        # The features supported by the instance. Valid values:
        # 
        # *   sample_data: sample dataset. For more information, see [Sample dataset](https://help.aliyun.com/document_detail/452278.html).
        # *   diagnose_and_optimize: diagnostics and optimization. For more information, see [Diagnostics and optimization](https://help.aliyun.com/document_detail/323453.html).
        self.support_feature_list = support_feature_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.support_feature_list is not None:
            result['SupportFeatureList'] = self.support_feature_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SupportFeatureList') is not None:
            self.support_feature_list = m.get('SupportFeatureList')

        return self

