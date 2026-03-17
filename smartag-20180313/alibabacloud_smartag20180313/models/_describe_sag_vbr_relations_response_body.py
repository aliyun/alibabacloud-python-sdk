# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_smartag20180313 import models as main_models
from darabonba.model import DaraModel

class DescribeSagVbrRelationsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        sag_vbr_relations: List[main_models.DescribeSagVbrRelationsResponseBodySagVbrRelations] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the specified VBR is associated with an SAG instance.
        self.sag_vbr_relations = sag_vbr_relations

    def validate(self):
        if self.sag_vbr_relations:
            for v1 in self.sag_vbr_relations:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SagVbrRelations'] = []
        if self.sag_vbr_relations is not None:
            for k1 in self.sag_vbr_relations:
                result['SagVbrRelations'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.sag_vbr_relations = []
        if m.get('SagVbrRelations') is not None:
            for k1 in m.get('SagVbrRelations'):
                temp_model = main_models.DescribeSagVbrRelationsResponseBodySagVbrRelations()
                self.sag_vbr_relations.append(temp_model.from_map(k1))

        return self

class DescribeSagVbrRelationsResponseBodySagVbrRelations(DaraModel):
    def __init__(
        self,
        sag_instance_id: str = None,
        sag_uid: str = None,
        vbr_instance_id: str = None,
    ):
        # The ID of the SAG instance.
        self.sag_instance_id = sag_instance_id
        # The ID of the Alibaba Cloud account to which the SAG instance belongs.
        self.sag_uid = sag_uid
        # The ID of the VBR.
        self.vbr_instance_id = vbr_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.sag_instance_id is not None:
            result['SagInstanceId'] = self.sag_instance_id

        if self.sag_uid is not None:
            result['SagUid'] = self.sag_uid

        if self.vbr_instance_id is not None:
            result['VbrInstanceId'] = self.vbr_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SagInstanceId') is not None:
            self.sag_instance_id = m.get('SagInstanceId')

        if m.get('SagUid') is not None:
            self.sag_uid = m.get('SagUid')

        if m.get('VbrInstanceId') is not None:
            self.vbr_instance_id = m.get('VbrInstanceId')

        return self

