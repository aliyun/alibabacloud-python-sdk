# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eas20210701 import models as main_models
from darabonba.model import DaraModel

class ListServiceVersionsResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        versions: List[main_models.ListServiceVersionsResponseBodyVersions] = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count
        # The historical versions of the service.
        self.versions = versions

    def validate(self):
        if self.versions:
            for v1 in self.versions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        result['Versions'] = []
        if self.versions is not None:
            for k1 in self.versions:
                result['Versions'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        self.versions = []
        if m.get('Versions') is not None:
            for k1 in m.get('Versions'):
                temp_model = main_models.ListServiceVersionsResponseBodyVersions()
                self.versions.append(temp_model.from_map(k1))

        return self

class ListServiceVersionsResponseBodyVersions(DaraModel):
    def __init__(
        self,
        build_time: str = None,
        image_available: str = None,
        image_id: int = None,
        message: str = None,
        service_config: str = None,
        service_runnable: str = None,
    ):
        # The time when the service version was created. The time is displayed in UTC.
        self.build_time = build_time
        # Indicates whether the image is available. Valid values:
        # 
        # *   true: The image is available.
        # *   false: The image is unavailable.
        # *   unknown: The availability of the image is unknown.
        self.image_available = image_available
        # The image ID.
        self.image_id = image_id
        # The returned message.
        self.message = message
        # The service deployment configurations. This parameter is returned only if the service is deployed by using a custom image.
        self.service_config = service_config
        # Indicates whether Elastic Algorithm service (EAS) is activated. Valid values:
        # 
        # *   true: EAS is activated.
        # *   false: EAS is not activated.
        # *   unknown: The activation of EAS is unknown.
        self.service_runnable = service_runnable

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.build_time is not None:
            result['BuildTime'] = self.build_time

        if self.image_available is not None:
            result['ImageAvailable'] = self.image_available

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.message is not None:
            result['Message'] = self.message

        if self.service_config is not None:
            result['ServiceConfig'] = self.service_config

        if self.service_runnable is not None:
            result['ServiceRunnable'] = self.service_runnable

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BuildTime') is not None:
            self.build_time = m.get('BuildTime')

        if m.get('ImageAvailable') is not None:
            self.image_available = m.get('ImageAvailable')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('ServiceConfig') is not None:
            self.service_config = m.get('ServiceConfig')

        if m.get('ServiceRunnable') is not None:
            self.service_runnable = m.get('ServiceRunnable')

        return self

