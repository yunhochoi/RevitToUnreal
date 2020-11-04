# Architectural Visualization

## Resources

Free PBR (physically based rendering) materials:

[https://freepbr.com/](https://www.youtube.com/redirect?q=https%3A%2F%2Ffreepbr.com%2F&v=aI0J3Im_JDw&redir_token=QUFFLUhqbmRaYWU2X2hicDBXLUdnWTZQVjU4OFd5LV9zUXxBQ3Jtc0ttWEZKZUdObk85UUhLNlpGVjRsMzdFZ0lZS3BFVXlPVlNEanVFVVN4VnNDV2NoNWcxSWs4WllHelJfX3gzN0FXUm1uVTZUcWZ1QlY1SU04RnlyR3dkNXpvT1ZZSzE0YVo4TUJQVm96WkV5MlZYNXJvOA%3D%3D&event=video_description)

Free HDRI (high dynamic range images) :

[https://hdrihaven.com/](https://www.youtube.com/redirect?q=https%3A%2F%2Fhdrihaven.com%2F&v=aI0J3Im_JDw&redir_token=QUFFLUhqbnB6endQWkNZSWtJNkNKYlpaTmhoMF9uUjJqQXxBQ3Jtc0tuaWU4cFV0S1Y1Uzg0UXFxZHdJaGYwTmFzNDI2MjBZZDA3NXlncjBDZzN1M0U4RFFkVjl2M1Z1NWQ4ajRna200RmlYOHMxTW5FdW1mSUlyaThDdHVkdFpIbXRVZDRNV1hxOUNiZWtjM05fRlFESDZ5VQ%3D%3D&event=video_description)

Starter Revit file:

[https://goo.gl/NEuusM](https://www.youtube.com/redirect?q=https%3A%2F%2Fgoo.gl%2FNEuusM&v=aI0J3Im_JDw&redir_token=QUFFLUhqa0JPbksyN0trOWtEcjNKajFybVltTnNCN2FnQXxBQ3Jtc0trUWRLdUxZSGZkbkhrT2NJNFF3NWxZODUta3dUVFZIQnRpdnZma3czSnRiOGU2R09lR0thMTJQUlZCNXladWhCMW1qbUkxNzktSzZIV1VoUVE5TU8xZ2c4MGlTSVp0SkN6VWpfdGhWSmxZcm9MUmp3aw%3D%3D&event=video_description)

[Unreal Engine 4 + GitHub First Steps](https://odederell3d.blog/2020/04/22/unreal-engine-4-github-first-steps/)

[Interactive Architectural Visualization in Unreal Engine | Autodesk University 2019 | Unreal Engine](https://www.youtube.com/watch?v=o_2Q5y1AXVI)

[Unreal Engine: Arch Viz Training (Pt. 1)](https://www.youtube.com/watch?v=aI0J3Im_JDw)

# Project Setup

### Essential Plugins

- [Datasmith](https://www.unrealengine.com/marketplace/ko/product/unreal-datasmith#)
- Substance (material, need to subscribe)

### Project Setting

- preset is saved in Config/DefaultEngine.ini - can be used like loom
- Change light unit to lumen
- Disable auto exposure(Mac didn't work) and ambient occlusion

### Editor Preference

- Load-save: Disable Auto-save

# Environment Setup

## Import 3D Model From Revit

- At Revit: Always take large object into smaller pieces and then export to Datasmith format (Add-in tap → Export 3D View)
- At Unreal: import the Datasmith file

![Architectural%20Visualization%20f78a7674279e48268b34b851fe5e36ad/Untitled.png](Architectural%20Visualization%20f78a7674279e48268b34b851fe5e36ad/Untitled.png)

![Architectural%20Visualization%20f78a7674279e48268b34b851fe5e36ad/Untitled%201.png](Architectural%20Visualization%20f78a7674279e48268b34b851fe5e36ad/Untitled%201.png)

## Add Lightmass Importance Volume, Post Processing Volume, Sphere Reflection Capture

![Architectural%20Visualization%20f78a7674279e48268b34b851fe5e36ad/Untitled%202.png](Architectural%20Visualization%20f78a7674279e48268b34b851fe5e36ad/Untitled%202.png)

![Architectural%20Visualization%20f78a7674279e48268b34b851fe5e36ad/Untitled%203.png](Architectural%20Visualization%20f78a7674279e48268b34b851fe5e36ad/Untitled%203.png)

![Architectural%20Visualization%20f78a7674279e48268b34b851fe5e36ad/Untitled%204.png](Architectural%20Visualization%20f78a7674279e48268b34b851fe5e36ad/Untitled%204.png)

## Add or Change HRDI Background

- Download an asset in hdrihave.com
- Import and refine image (brightness 0.2, NoMipmaps of level of details)

    ![Architectural%20Visualization%20f78a7674279e48268b34b851fe5e36ad/Untitled%205.png](Architectural%20Visualization%20f78a7674279e48268b34b851fe5e36ad/Untitled%205.png)

- Edit SkySphereMaterial

    ![Architectural%20Visualization%20f78a7674279e48268b34b851fe5e36ad/Untitled%206.png](Architectural%20Visualization%20f78a7674279e48268b34b851fe5e36ad/Untitled%206.png)

- Add skylight and insert the HDRI texture to Cubemap and set source type to SLS specified Cubemap
    - [ ]  Sunsky (generates shadow) and EditorSphereSky need to co-exist

    ![Architectural%20Visualization%20f78a7674279e48268b34b851fe5e36ad/Untitled%207.png](Architectural%20Visualization%20f78a7674279e48268b34b851fe5e36ad/Untitled%207.png)

## Setup GPU Lightmass

- Force your GPU to engege lightmass calculation reducing hours of render time to minutes
- Visit this link and find a proper one that fits with your Unreal version
- Download and overwrite the files under Unreal_version/Engine folder
- There might be a built-in GPU lightmass from version 4.6x

[Luoshuang's GPULightmass](https://forums.unrealengine.com/development-discussion/rendering/1460002-luoshuang-s-gpulightmass)

[UnrealEngine - GPU lightmass vs CPU lightmass](https://www.youtube.com/watch?v=d1egga-FPeA)

## Build Lighting with GPU

![Architectural%20Visualization%20f78a7674279e48268b34b851fe5e36ad/Untitled%208.png](Architectural%20Visualization%20f78a7674279e48268b34b851fe5e36ad/Untitled%208.png)

![Architectural%20Visualization%20f78a7674279e48268b34b851fe5e36ad/Untitled%209.png](Architectural%20Visualization%20f78a7674279e48268b34b851fe5e36ad/Untitled%209.png)

- To restore default lightmass values: Launch Unreal with verify option

    ![Architectural%20Visualization%20f78a7674279e48268b34b851fe5e36ad/Untitled%2010.png](Architectural%20Visualization%20f78a7674279e48268b34b851fe5e36ad/Untitled%2010.png)

# Material and Lighting

## Replace Basic Materials from Revit to Unreal

Sometimes the materials directly imported from Revit are not the best quality, so it is recommended to replace with Unreal's standard materials so you can start your project with better-looking scene.

### Instance Material

- Create 'Materials' folder under Content.
- Go to Content > StarterContent > Material and select a new material that you want replace
- Click 'Create Material Instance' and drag the material instance to the Content > Materials folder.

![Architectural%20Visualization%20f78a7674279e48268b34b851fe5e36ad/Untitled%2011.png](Architectural%20Visualization%20f78a7674279e48268b34b851fe5e36ad/Untitled%2011.png)

![Architectural%20Visualization%20f78a7674279e48268b34b851fe5e36ad/Untitled%2012.png](Architectural%20Visualization%20f78a7674279e48268b34b851fe5e36ad/Untitled%2012.png)

### Option A. Manual Replacement

- Choose a 3D element that you want to be replaced and then see where the material is located in the asset folder
- In Delete Assets window, click Replace References and select a new material
- Click the material and hit delete key

![Architectural%20Visualization%20f78a7674279e48268b34b851fe5e36ad/Untitled%2013.png](Architectural%20Visualization%20f78a7674279e48268b34b851fe5e36ad/Untitled%2013.png)

### Option B. Batch Replacement by Python

- Create a python script and execute in Unreal

    ```python
    import unreal

    def replaceMaterial(original, replacement) :

        print "hello"
        original_asset = unreal.EditorAssetLibrary.load_asset(original)
        replacement_asset = unreal.EditorAssetLibrary.load_asset(replacement)
        unreal.EditorAssetLibrary.consolidate_assets(replacement_asset,[original_asset])

    # Game: Content folder
    replaceMaterial('/Game/Technical_school-current_m-3DView-From_Parking_Area/Materials/Glass','/Game/Materials/M_Glass_Inst')
    ```

    ![Architectural%20Visualization%20f78a7674279e48268b34b851fe5e36ad/Untitled%2014.png](Architectural%20Visualization%20f78a7674279e48268b34b851fe5e36ad/Untitled%2014.png)

## Light Adjustment

- Select and group light bulbs (Ctrl + G) that you want to adjust

- Adjustment color, intensity, and attenuation radius

    ![Architectural%20Visualization%20f78a7674279e48268b34b851fe5e36ad/Untitled%2015.png](Architectural%20Visualization%20f78a7674279e48268b34b851fe5e36ad/Untitled%2015.png)

- In you don't see the light in the scene, you can change the mobility from Static to Movable

    ![Architectural%20Visualization%20f78a7674279e48268b34b851fe5e36ad/Untitled%2016.png](Architectural%20Visualization%20f78a7674279e48268b34b851fe5e36ad/Untitled%2016.png)