# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListRegionIdRequest(DaraModel):
    def __init__(
        self,
        product_type: str = None,
    ):
        # The product type for querying available image regions. If this parameter is omitted, the query defaults to CloudApp. Valid values:
        # - **CloudGame**: cloud gaming
        # - **CloudApp**: WUYING Cloud Application
        # - **CloudBrowser**: secure browser
        # - **CloudDesktop**: WUYING Cloud Desktop
        # - **ImageBuilder**: image creation resources
        # - **ImageValidate**: image validation resources
        # - **AndroidCloud**: Android cloud
        # - **GpuRender**: GPU rendering
        # - **AndroidGpuRender**: Android cloud GPU rendering
        # - **WuyingServer**: enterprise edition workstation
        # - **GpuProxy**: GPU remote rendering proxy
        # - **GpuCache**: GPU remote rendering cache
        # - **AIAgent**: AI agent service
        # - **HostedDesktop**: hosted desktop
        # - **WuyingWorkstation**: personal edition container workstation
        # - **WuyingWorkstationBusiness**: business edition container workstation
        # - **WuyingWorkstationTeam**: Linggou container workstation team edition
        self.product_type = product_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.product_type is not None:
            result['ProductType'] = self.product_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        return self

