# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PublicSyncAndCreateImageScanTaskRequest(DaraModel):
    def __init__(
        self,
        images: str = None,
        source_ip: str = None,
    ):
        # The information about the images. The value of this parameter is in the JSON format and contains the following fields:
        # 
        # *   **RegistryType**: the type of the image repository. Valid values:
        # 
        #     *   acr
        #     *   harbor
        #     *   quay
        # 
        # *   **RepoId**: the ID of the image repository.
        # 
        # *   **InstanceId**: the ID of the Container Registry instance to which the image repository belongs.
        # 
        # *   **RepoNamespace**: the namespace to which the image repository belongs.
        # 
        # *   **RegionId**: the region ID of the image.
        # 
        # *   **RepoName**: the name of the image repository.
        # 
        # *   **Digest**: the digest of the image.
        # 
        # *   **Tag**: the tag that is added to the image.
        # 
        # *   **CreateTime**: the timestamp when the image was created. Unit: milliseconds.
        # 
        # *   **UpdateTime**: the timestamp when the image was updated. Unit: milliseconds.
        # 
        # This parameter is required.
        self.images = images
        # The source IP address of the request.
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.images is not None:
            result['Images'] = self.images

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Images') is not None:
            self.images = m.get('Images')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        return self

