# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class ListDockerhubImageResponseBody(DaraModel):
    def __init__(
        self,
        image_list: List[main_models.ListDockerhubImageResponseBodyImageList] = None,
        request_id: str = None,
    ):
        # The information about the images.
        self.image_list = image_list
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.image_list:
            for v1 in self.image_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ImageList'] = []
        if self.image_list is not None:
            for k1 in self.image_list:
                result['ImageList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.image_list = []
        if m.get('ImageList') is not None:
            for k1 in m.get('ImageList'):
                temp_model = main_models.ListDockerhubImageResponseBodyImageList()
                self.image_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListDockerhubImageResponseBodyImageList(DaraModel):
    def __init__(
        self,
        digest: str = None,
        hc_count: int = None,
        image_id: str = None,
        image_size: int = None,
        repo_name: str = None,
        repo_namespace: str = None,
        risk_level_detail: str = None,
        tag: str = None,
        uuid: str = None,
        vul_count: int = None,
    ):
        # The digest value of the image.
        self.digest = digest
        # The number of baseline risks.
        self.hc_count = hc_count
        # The image ID.
        self.image_id = image_id
        # The size of the image. Unit: bytes.
        self.image_size = image_size
        # The name of the image repository.
        self.repo_name = repo_name
        # The namespace to which the image repository belongs.
        self.repo_namespace = repo_namespace
        # The risk details of the image.
        self.risk_level_detail = risk_level_detail
        # The tag of the image.
        self.tag = tag
        # The UUID of the image.
        self.uuid = uuid
        # The number of detected vulnerabilities.
        self.vul_count = vul_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.digest is not None:
            result['Digest'] = self.digest

        if self.hc_count is not None:
            result['HcCount'] = self.hc_count

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.image_size is not None:
            result['ImageSize'] = self.image_size

        if self.repo_name is not None:
            result['RepoName'] = self.repo_name

        if self.repo_namespace is not None:
            result['RepoNamespace'] = self.repo_namespace

        if self.risk_level_detail is not None:
            result['RiskLevelDetail'] = self.risk_level_detail

        if self.tag is not None:
            result['Tag'] = self.tag

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        if self.vul_count is not None:
            result['VulCount'] = self.vul_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Digest') is not None:
            self.digest = m.get('Digest')

        if m.get('HcCount') is not None:
            self.hc_count = m.get('HcCount')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('ImageSize') is not None:
            self.image_size = m.get('ImageSize')

        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')

        if m.get('RepoNamespace') is not None:
            self.repo_namespace = m.get('RepoNamespace')

        if m.get('RiskLevelDetail') is not None:
            self.risk_level_detail = m.get('RiskLevelDetail')

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        if m.get('VulCount') is not None:
            self.vul_count = m.get('VulCount')

        return self

