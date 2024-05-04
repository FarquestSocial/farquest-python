# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from farquest import Farquest, AsyncFarquest
from farquest._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestQuest:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Farquest) -> None:
        quest = client.quest.create(
            description="string",
            ends_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            image="string",
            name="string",
            organization_id="string",
            quest_type_id="string",
            starts_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            validation_criteria={},
        )
        assert quest is None

    @parametrize
    def test_method_create_with_all_params(self, client: Farquest) -> None:
        quest = client.quest.create(
            description="string",
            ends_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            image="string",
            name="string",
            organization_id="string",
            quest_type_id="string",
            starts_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            validation_criteria={},
            custom_callback_metadata={},
            custom_metadata={},
        )
        assert quest is None

    @parametrize
    def test_raw_response_create(self, client: Farquest) -> None:
        response = client.quest.with_raw_response.create(
            description="string",
            ends_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            image="string",
            name="string",
            organization_id="string",
            quest_type_id="string",
            starts_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            validation_criteria={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        quest = response.parse()
        assert quest is None

    @parametrize
    def test_streaming_response_create(self, client: Farquest) -> None:
        with client.quest.with_streaming_response.create(
            description="string",
            ends_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            image="string",
            name="string",
            organization_id="string",
            quest_type_id="string",
            starts_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            validation_criteria={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            quest = response.parse()
            assert quest is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Farquest) -> None:
        quest = client.quest.retrieve(
            "string",
        )
        assert quest is None

    @parametrize
    def test_raw_response_retrieve(self, client: Farquest) -> None:
        response = client.quest.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        quest = response.parse()
        assert quest is None

    @parametrize
    def test_streaming_response_retrieve(self, client: Farquest) -> None:
        with client.quest.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            quest = response.parse()
            assert quest is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Farquest) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.quest.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Farquest) -> None:
        quest = client.quest.list(
            "ACTIVE",
        )
        assert quest is None

    @parametrize
    def test_method_list_with_all_params(self, client: Farquest) -> None:
        quest = client.quest.list(
            "ACTIVE",
        )
        assert quest is None

    @parametrize
    def test_raw_response_list(self, client: Farquest) -> None:
        response = client.quest.with_raw_response.list(
            "ACTIVE",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        quest = response.parse()
        assert quest is None

    @parametrize
    def test_streaming_response_list(self, client: Farquest) -> None:
        with client.quest.with_streaming_response.list(
            "ACTIVE",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            quest = response.parse()
            assert quest is None

        assert cast(Any, response.is_closed) is True


class TestAsyncQuest:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncFarquest) -> None:
        quest = await async_client.quest.create(
            description="string",
            ends_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            image="string",
            name="string",
            organization_id="string",
            quest_type_id="string",
            starts_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            validation_criteria={},
        )
        assert quest is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncFarquest) -> None:
        quest = await async_client.quest.create(
            description="string",
            ends_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            image="string",
            name="string",
            organization_id="string",
            quest_type_id="string",
            starts_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            validation_criteria={},
            custom_callback_metadata={},
            custom_metadata={},
        )
        assert quest is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncFarquest) -> None:
        response = await async_client.quest.with_raw_response.create(
            description="string",
            ends_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            image="string",
            name="string",
            organization_id="string",
            quest_type_id="string",
            starts_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            validation_criteria={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        quest = await response.parse()
        assert quest is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncFarquest) -> None:
        async with async_client.quest.with_streaming_response.create(
            description="string",
            ends_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            image="string",
            name="string",
            organization_id="string",
            quest_type_id="string",
            starts_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            validation_criteria={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            quest = await response.parse()
            assert quest is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncFarquest) -> None:
        quest = await async_client.quest.retrieve(
            "string",
        )
        assert quest is None

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncFarquest) -> None:
        response = await async_client.quest.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        quest = await response.parse()
        assert quest is None

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncFarquest) -> None:
        async with async_client.quest.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            quest = await response.parse()
            assert quest is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncFarquest) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.quest.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncFarquest) -> None:
        quest = await async_client.quest.list(
            "ACTIVE",
        )
        assert quest is None

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncFarquest) -> None:
        quest = await async_client.quest.list(
            "ACTIVE",
        )
        assert quest is None

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncFarquest) -> None:
        response = await async_client.quest.with_raw_response.list(
            "ACTIVE",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        quest = await response.parse()
        assert quest is None

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncFarquest) -> None:
        async with async_client.quest.with_streaming_response.list(
            "ACTIVE",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            quest = await response.parse()
            assert quest is None

        assert cast(Any, response.is_closed) is True
