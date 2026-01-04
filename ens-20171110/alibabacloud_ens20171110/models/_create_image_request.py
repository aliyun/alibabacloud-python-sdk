# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateImageRequest(DaraModel):
    def __init__(
        self,
        delete_after_image_upload: str = None,
        image_name: str = None,
        instance_id: str = None,
        snapshot_id: str = None,
        target_ossregion_id: str = None,
        with_data_disks: bool = None,
    ):
        # Specifies whether to automatically release the instance after the image is packaged and uploaded. Only image builders are supported. Default value: false. Valid values:
        # 
        # *   true: The image is released when the instance is released.
        # *   false: The image is retained when the instance is released.
        # *   If you leave this property empty, false is used by default.
        self.delete_after_image_upload = delete_after_image_upload
        # The name of the image. The name must be 2 to 128 characters in length. The name can contain letters, digits, colons (:), underscores (_), and hyphens (-). It must start with a letter but cannot start with `http://` or `https://`. The name can contain letters, digits, colons (:), underscores (_), and hyphens (-).
        # 
        # This parameter is required.
        self.image_name = image_name
        # The ID of the instance.
        self.instance_id = instance_id
        # The ID of the snapshot.
        self.snapshot_id = snapshot_id
        # The region of the destination OSS bucket where the image is to be stored.
        self.target_ossregion_id = target_ossregion_id
        # Specifies whether to include data disk snapshots in the custom image.
        self.with_data_disks = with_data_disks

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.delete_after_image_upload is not None:
            result['DeleteAfterImageUpload'] = self.delete_after_image_upload

        if self.image_name is not None:
            result['ImageName'] = self.image_name

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id

        if self.target_ossregion_id is not None:
            result['TargetOSSRegionId'] = self.target_ossregion_id

        if self.with_data_disks is not None:
            result['WithDataDisks'] = self.with_data_disks

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeleteAfterImageUpload') is not None:
            self.delete_after_image_upload = m.get('DeleteAfterImageUpload')

        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')

        if m.get('TargetOSSRegionId') is not None:
            self.target_ossregion_id = m.get('TargetOSSRegionId')

        if m.get('WithDataDisks') is not None:
            self.with_data_disks = m.get('WithDataDisks')

        return self

