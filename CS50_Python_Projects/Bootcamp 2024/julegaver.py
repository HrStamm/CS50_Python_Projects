
Anna_gave,Laura_gave,Oscar_gave = map(int,input("Hvor mange gaver fik Anna, Laura og Oscar: ").split())


if 0 < Anna_gave > 100 or 0 < Laura_gave > 100 or 0 < Oscar_gave > 100:
    print("kan ikke modtage mindre end 0 eller flere end 100 gaver")
elif Anna_gave < Oscar_gave and Anna_gave < Laura_gave:
    print("Anna bliver sur")
elif Laura_gave < Anna_gave:
    print("Laura bliver sur")
elif Oscar_gave < Anna_gave or Oscar_gave < Laura_gave:
    print("Oscar bliver sur")
else:
    print("ingen bliver sure")
