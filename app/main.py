from typing import List
from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError



def go_to_cafe(friends: List[dict], cafe: Cafe) -> str:
    masks_to_buy = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            # If any friend is unvaccinated or has an outdated vaccine
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            # Count friends without masks
            masks_to_buy += 1

    # Determine the final message based on mask count
    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"
    return f"Friends can go to {cafe.name}"
