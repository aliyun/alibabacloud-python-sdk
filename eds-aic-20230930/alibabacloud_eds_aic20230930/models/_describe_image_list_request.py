# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eds_aic20230930 import models as main_models
from darabonba.model import DaraModel

class DescribeImageListRequest(DaraModel):
    def __init__(
        self,
        image_biz_tags: List[main_models.DescribeImageListRequestImageBizTags] = None,
        image_id: str = None,
        image_name: str = None,
        image_package_type: str = None,
        image_type: str = None,
        instance_type: str = None,
        max_results: int = None,
        next_token: str = None,
        status: str = None,
        system_type: str = None,
    ):
        self.image_biz_tags = image_biz_tags
        # The ID of the image.
        self.image_id = image_id
        # The name of the image.
        self.image_name = image_name
        # Image package type.
        self.image_package_type = image_package_type
        # The type of the image.
        # 
        # Valid values:
        # 
        # *   User: custom images.
        # *   System: system images.
        # 
        # This parameter is required.
        self.image_type = image_type
        self.instance_type = instance_type
        # The number of entries per page. Valid values: 1 to 100. Default value: 20.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. If the parameter is left empty, the data is queried from the first entry.
        self.next_token = next_token
        # The state of the image.
        # 
        # Valid values:
        # 
        # *   AVAILABLE: The image is available.
        # *   DELETE: The image is deleted.
        # *   INIT: The image is being initialized.
        # *   CREATE_FAILED: The image failed to be created.
        # *   CREATING: The image is being created.
        self.status = status
        self.system_type = system_type

    def validate(self):
        if self.image_biz_tags:
            for v1 in self.image_biz_tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ImageBizTags'] = []
        if self.image_biz_tags is not None:
            for k1 in self.image_biz_tags:
                result['ImageBizTags'].append(k1.to_map() if k1 else None)

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.image_name is not None:
            result['ImageName'] = self.image_name

        if self.image_package_type is not None:
            result['ImagePackageType'] = self.image_package_type

        if self.image_type is not None:
            result['ImageType'] = self.image_type

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.status is not None:
            result['Status'] = self.status

        if self.system_type is not None:
            result['SystemType'] = self.system_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.image_biz_tags = []
        if m.get('ImageBizTags') is not None:
            for k1 in m.get('ImageBizTags'):
                temp_model = main_models.DescribeImageListRequestImageBizTags()
                self.image_biz_tags.append(temp_model.from_map(k1))

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')

        if m.get('ImagePackageType') is not None:
            self.image_package_type = m.get('ImagePackageType')

        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SystemType') is not None:
            self.system_type = m.get('SystemType')

        return self

class DescribeImageListRequestImageBizTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

