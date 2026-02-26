# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class OctreeOption(DaraModel):
    def __init__(
        self,
        do_voxel_grid_down_down_sampling: bool = None,
        library_name: str = None,
        octree_resolution: float = None,
        point_resolution: float = None,
    ):
        # Specifies whether to downsample the point cloud file. Valid values:
        # 
        # *   true: The point cloud file is downsampled, and the coordinates of the points in a voxel are replaced with the coordinates of the center point of the voxel. The average color of all points in the voxel is used as the color of the voxel. In this case, the PointResolution parameter does not take effect.
        # *   false: Specific coordinates and colors in a voxel are encoded by calculating the offsets from each point to the lower-left corner of the voxel. The offsets are divided by the PointResolution value to obtain the integer coordinates. The residual of the color for each point relative to the average color of all points in the voxel is encoded.
        self.do_voxel_grid_down_down_sampling = do_voxel_grid_down_down_sampling
        # The library name. Set the value to pcl. Default value: pcl.
        self.library_name = library_name
        # The minimum block size when an octree is partitioned. The minimum block size indicates the edge length of a voxel. Default value: 0.01.
        self.octree_resolution = octree_resolution
        # The point cloud resolution. This parameter determines the precision of the point coordinates during encoding. Default value: 0.01.
        self.point_resolution = point_resolution

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.do_voxel_grid_down_down_sampling is not None:
            result['DoVoxelGridDownDownSampling'] = self.do_voxel_grid_down_down_sampling

        if self.library_name is not None:
            result['LibraryName'] = self.library_name

        if self.octree_resolution is not None:
            result['OctreeResolution'] = self.octree_resolution

        if self.point_resolution is not None:
            result['PointResolution'] = self.point_resolution

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DoVoxelGridDownDownSampling') is not None:
            self.do_voxel_grid_down_down_sampling = m.get('DoVoxelGridDownDownSampling')

        if m.get('LibraryName') is not None:
            self.library_name = m.get('LibraryName')

        if m.get('OctreeResolution') is not None:
            self.octree_resolution = m.get('OctreeResolution')

        if m.get('PointResolution') is not None:
            self.point_resolution = m.get('PointResolution')

        return self

