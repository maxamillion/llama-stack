# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

from typing import Any

from pydantic import BaseModel, ConfigDict

from llama_stack.schema_utils import json_schema_type


@json_schema_type
class MilvusVectorIOConfig(BaseModel):
    uri: str
    token: str | None = None
    consistency_level: str = "Strong"

    model_config = ConfigDict(extra="allow")

    @classmethod
    def sample_run_config(cls, __distro_dir__: str, **kwargs: Any) -> dict[str, Any]:
        return {"uri": "${env.MILVUS_ENDPOINT}", "token": "${env.MILVUS_TOKEN}"}
