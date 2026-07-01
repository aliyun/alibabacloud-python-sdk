# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ververica20220718 import models as main_models
from darabonba.model import DaraModel

class StartJobRequest(DaraModel):
    def __init__(
        self,
        body: main_models.StartJobRequestBody = None,
    ):
        # Launch instance parameters.\\`LaunchInstance\\` is the API operation for creating one or more ECS instances.\\`LaunchInstance\\` is the API for creating one or more ECS instances.\\`LaunchInstance\\` is the API for creating one or more ECS instances.| Parameter | Type | Required | Example | Description |
        # \\| --- | --- | --- | --- | --- |
        # \\| \\`RegionId\\` | String | Yes | \\`cn-hangzhou\\` | The ID of the region where the instance resides. Call the [DescribeRegions]\\(\\~\\~25609\\~\\~) operation to view the latest list of Alibaba Cloud regions. |
        # \\| \\`InstanceType\\` | String | Yes | \\`ecs.g5.large\\` | The instance type. For more information, see [Instance families]\\(\\~\\~25378\\~\\~) or call the [DescribeInstanceTypes]\\(\\~\\~25620\\~\\~) operation to query the latest instance type list. |
        # \\| \\`ImageId\\` | String | Yes | \\`centos_7_04_64_20G_alibase_201701015.vhd\\` | The ID of the image to use for creating the instance. Call the [DescribeImages]\\(\\~\\~25619\\~\\~) operation to query available image resources. |
        # \\| \\`SecurityGroupId\\` | String | Yes | \\`sg-bp15ed6xe1yxeycg7\\*\\*\\*\\` | The ID of the security group for the new instance. Instances within the same security group can communicate with each other over the internal network. |
        # \\| \\`InstanceName\\` | String | No | \\`testInstanceName\\` | The display name of the instance. The name must be 2 to 128 characters long and start with a letter or a Chinese character. It can contain digits, underscores (\\`_\\`), hyphens (\\`-\\`), and periods (\\`.\\`). |
        # \\| \\`Description\\` | String | No | \\`testDescription\\` | The description of the instance. The description must be 2 to 256 characters long. |
        # \\| \\`InternetMaxBandwidthOut\\` | Integer | No | 100 | The maximum outbound public bandwidth, in Mbit/s. Valid values:If the billing method is pay-by-bandwidth (\\`PayByBandwidth\\`): 0 to 100. The default value is 0.If the billing method is pay-by-traffic (\\`PayByTraffic\\`): 0 to 100. The default value is 0. |
        # \\| \\`HostName\\` | String | No | \\`testHostName\\` | The hostname of the instance.Periods (\\`.\\`) and hyphens (\\`-\\`) cannot be used at the beginning or end of the hostname. They also cannot be used consecutively.For Windows instances: The hostname must be 2 to 15 characters long. It can contain letters, digits, and hyphens (\\`-\\`). It cannot contain periods (\\`.\\`) or consist entirely of digits.For other instance types (such as Linux): The hostname must be 2 to 64 characters long. It can contain periods (\\`.\\`) and hyphens (\\`-\\`). Use periods to separate the hostname into segments. Each segment can contain letters, digits, and hyphens (\\`-\\`). |
        # \\| \\`Password\\` | String | No | \\`Ecs\\@123\\` | The login password for the instance. The password must be 8 to 30 characters long and contain characters from at least three of the following categories: uppercase letters, lowercase letters, digits, and special characters. Allowed special characters are:\\`( ) \\` \\~ ! @ # $ % ^ & \\* - _ + = | { } [ ] : ; \\" < > , . ? /\\`For Windows instances, the password cannot start with a forward slash (\\`/\\`). |
        # \\| \\`ZoneId\\` | String | No | \\`cn-hangzhou-b\\` | The ID of the zone for the instance. For more information, see the [DescribeZones]\\(\\~\\~25610\\~\\~) operation. |
        # \\| \\`IoOptimized\\` | String | No | \\`optimized\\` | Specifies whether the instance is I/O optimized. Only I/O optimized instances can use SSD cloud disks.\\`none\\`: Not I/O optimized.\\`optimized\\`: I/O optimized.For more information, see [I/O optimization]\\(\\~\\~57943\\~\\~). |
        # \\| \\`SystemDisk.Category\\` | String | No | \\`cloud_ssd\\` | The category of the system disk. Valid values:\\`cloud_efficiency\\`: Ultra Disk.\\`cloud_ssd\\`: Standard SSD.\\`cloud_essd\\`: Enhanced SSD (ESSD).\\`cloud\\`: Basic Disk.The default value is \\`cloud_efficiency\\` for I/O optimized instances and \\`cloud\\` for non-I/O optimized instances. |
        # \\| \\`SystemDisk.Size\\` | Integer | No | 40 | The size of the system disk, in GiB. Valid values: 20 to 500.The value must be greater than or equal to \\`max(20, ImageSize)\\`. |
        # \\| \\`SystemDisk.DiskName\\` | String | No | \\`testSystemDiskName\\` | The name of the system disk. |
        # \\| \\`SystemDisk.Description\\` | String | No | \\`testSystemDiskDescription\\` | The description of the system disk. |
        # \\| \\`DataDisk.n.Size\\` | Integer | No | 2000 | The size of data disk \\`n\\`, in GiB. The value of \\`n\\` ranges from 1 to 16. The value range of this parameter depends on the disk category:\\`cloud_efficiency\\`: 20 to 32,768\\`cloud_ssd\\`: 20 to 32,768\\`cloud_essd\\`: 20 to 32,768\\`cloud\\`: 5 to 2,000The value must be greater than or equal to \\`max(20, ImageSize)\\`. |
        # \\| \\`DataDisk.n.Category\\` | String | No | \\`cloud_ssd\\` | The category of data disk \\`n\\`. The value of \\`n\\` ranges from 1 to 16. Valid values:\\`cloud_efficiency\\`: Ultra Disk.\\`cloud_ssd\\`: Standard SSD.\\`cloud_essd\\`: Enhanced SSD (ESSD).\\`cloud\\`: Basic Disk.For I/O optimized instances, the default value is \\`cloud_efficiency\\`. |
        # \\| \\`DataDisk.n.SnapshotId\\` | String | No | \\`s-bp17441ohwka0yuh\\*\\*\\*\\*\\` | The ID of the snapshot to use for creating data disk \\`n\\`. The value of \\`n\\` ranges from 1 to 16. |
        # \\| \\`DataDisk.n.DiskName\\` | String | No | \\`testDataDiskName\\` | The name of data disk \\`n\\`. The value of \\`n\\` ranges from 1 to 16. |
        # \\| \\`DataDisk.n.Description\\` | String | No | \\`testDataDiskDescription\\` | The description of data disk \\`n\\`. The value of \\`n\\` ranges from 1 to 16. |
        # \\| \\`DataDisk.n.DeleteWithInstance\\` | Boolean | No | \\`true\\` | Specifies whether to release data disk \\`n\\` when the instance is released. The value of \\`n\\` ranges from 1 to 16. |
        # 
        # This parameter is required.
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body is not None:
            result['body'] = self.body.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = main_models.StartJobRequestBody()
            self.body = temp_model.from_map(m.get('body'))

        return self

